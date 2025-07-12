from validation_error import ValidationError, ValidationWarning

def test_error():
    error = ValidationError()
    assert error.message == "ValidationError"

def test_validation_warning():
    warning = ValidationError("", level="warning")
    assert isinstance(warning, ValidationWarning)
    assert warning.message == "ValidationWarning"

    warning = ValidationWarning()
    assert warning.message == "ValidationWarning"
