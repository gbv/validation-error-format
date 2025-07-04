# Data Validation Error Format

This repository contains the specification of a data format to report validation errors of digital objects.

The current, preliminary draft is made available at <https://gbv.github.io/validation-error-format/>.

## tl;dr

Errors have `message`, optional `level` and `types`, and `positions`. Positions can be given in multiple formats, for instance character position, line number, and line/column:

~~~json
{
  "message": "Malformed name at line 2 column 3: invalid character '*'",
  "level": "error",
  "types": [ "http://example.org/error-types/invalid-character" ],
  "position": {
    "char": "8",
    "line": "2", 
    "linecol": "2:3"
  }
}
~~~

Positions can also be nested *within* another position:

~~~json
{
  "message": "Malformed name at line 2 column 3 in file names.txt: invalid character '*'",  
  "position": [ {
    "format": "file", "value": "names.txt",
    "message": "Malformed name at line 2 column 3: invalid character '*'",
    "position": [
      { "format": "char", "value": "8" },
      { "format": "linecol", "value": "2:3" },
      {
        "format": "line", "value": "2",
        "message": "Malformed name at character 3: invalid character '*'", 
        "position": {
          "char": "3"
        }
      }
    ]
  } ]
}
~~~

Position can also be given with other formats such as XPath for XML, JSON Pointer for JSON, and row/column for tabular data.


