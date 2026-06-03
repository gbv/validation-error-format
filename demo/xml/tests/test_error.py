from validation_error import ValidationError, Locator

def test_locator():
    loc = Locator("offset", 0)
    assert isinstance(loc, Locator)
    assert str(loc) == "offset 0"
    assert loc.to_dict() == { "format": "offset", "value": "0" }
    assert loc.condense() == ("offset", "0")

    loc = Locator("offset", 7, [ValidationError()])
    assert loc.to_dict() == { "format": "offset", "value": "7", "errors": [ { } ] }

def test_error():
    error = ValidationError()
    assert not error.message
    assert str(error) == "ValidationError"
    assert error.to_dict() == { }
    assert error.to_dict(level=True) == { "level": "error" }

    error = ValidationError("oops!")
    assert str(error) == "ValidationError: oops!"
    assert error.to_dict() == { "message": "oops!" }

    error = ValidationError("!")
    assert error.message == "!"

    error = ValidationError(message="!", position=[ Locator("char", "3") ])
    assert error.to_dict() == { "message": "!", "position": { "char": "3" } }
    assert error.to_dict(condense=False) == { "message": "!", "position": [ { "format": "char", "value": "3" } ] }

    error = ValidationError(message="!", position= { "char": "3" })
    assert error.to_dict() == { "message": "!", "position": { "char": "3" } }

    error = ValidationError(position= [ { "format": "char", "value": "3" } ])
    assert error.to_dict() == { "position": { "char": "3" } }

# TODO: test nested errors
