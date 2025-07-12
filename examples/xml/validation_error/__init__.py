class ValidationError(Exception):
    """An Error of Data Validation Error Format."""

    def __new__(cls, message="", **fields):
        """Instantiate ValidationError or ValidationWarning."""
        level = ValidationWarning if fields.get("level") == "warning" else cls
        if cls == level:
            return Exception.__new__(cls, message, **fields)
        else:
            return level.__new__(level, message, **fields)

    def __init__(self, message="", **fields):
        self.message = message if message else self.__class__.__name__
        if len(fields.get("types",[])):
            self.types = fields["types"]
        if fields.get("position"):
            self.position = fields["position"]

    def __str__(self):
        # TODO: include position
        return f"{self.message}"


class ValidationWarning(ValidationError):
    """An Error of Data Validation Error Format with level "warning"."""

    def __init__(self, message="", **fields):
        super().__init__(message, **fields)
        self.level = "warning"


class Locator:
    """A Locator of Data Validation Error Format."""

    def __init__(self, format, value):
        self.format = format
        self.value = value

    def __str__(self):
        return f"{self.format} {self.value}"


class NestedLocator(Locator):
    """A Nested Locator of Data Validation Error Format."""

    # TODO

