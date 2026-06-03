class Locator:
    """Location within a document, defined by locator format (aka dimension) and locator value."""

    def __init__(self, format: str, value: str, errors=[]):
        self.format = format
        self.value = str(value)
        if not self.format or not self.value:
            raise ValueError("Locator must have locator format and locator value!")
        self.errors = [
            e if isinstance(e, ValidationError) else ValidationError(e) for e in errors
        ]

    def __str__(self):
        return f"{self.format} {self.value}"

    def to_dict(self):
        d = {"format": self.format, "value": self.value}
        if self.errors:
            d["errors"] = [e.to_dict() for e in self.errors]
        return d

    def condense(self):
        return (self.format, self.value)


class ValidationError(Exception):
    """An Error of Data Validation Error Format."""

    def __init__(self, message: str = "", **fields):
        self.message = str(message) or fields.get("message", "")
        self.types = fields.get("types", [])
        self.level = fields.get("level", "error")
        position = fields.get("position", [])
        if type(position) == dict:  # expand condense form
            position = [Locator(k, v) for (k, v) in position.items()]
        else:
            position = [
                loc if isinstance(loc, Locator) else Locator(**loc) for loc in position
            ]
        self.position = position

    def __str__(self):
        cls = "ValidationError" if self.level == "error" else "ValidationWarning"
        return f"{cls}: {self.message}" if self.message else cls

    def to_dict(self, level=False, condense=True):
        d = {}
        if self.message:
            d["message"] = self.message
        if self.types:
            d["types"] = self.types
        if self.level and level:
            d["level"] = self.level
        if self.position:
            position = self.position
            if condense and condenseable(position):
                d["position"] = dict([p.condense() for p in position])
            else:
                d["position"] = [p.to_dict() for p in position]
        return d


def condenseable(position):
    if any([p.errors for p in position]):
        return False
    formats = [p.format for p in position]
    return len(formats) == len(set(formats))
