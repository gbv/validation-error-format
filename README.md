# Data Validation Error Format

This repository contains the specification of a data format to report validation errors of digital objects.

The current draft is made available at <https://gbv.github.io/validation-error-format/>.

## tl;dr

Errors have a `message`, optional `level`, `types`, and a `position`. The position can be given in with multiple locators, for instance by character position, line number, and line/column:

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

Locators of a position can also given as array, each with `dimension` and `address`:

~~~json
{
  "message": "Malformed name at line 2 column 3: invalid character '*'",
  "level": "error",
  "types": [ "http://example.org/error-types/invalid-character" ],
  "position": [
    { "dimension": "char", "address": "8" },
    { "dimension": "line": "address": "2" },
    { "dimension": "linecol": "address": "2:3" }
  ]
}
~~~

Each dimension refers to a locator format, suitable for some document models, for instance XPath for XML, JSON Pointer for JSON, and row/column for tabular data.

Locators can contain nested errors within the addressed part of a document:

~~~json
{
  "message": "Malformed name at line 2 column 3 in file names.txt: invalid character '*'",  
  "position": [
    {
      "dimension": "file", "address": "names.txt",
      "message": "Malformed name at line 2 column 3: invalid character '*'",
      "position": [
        { "dimension": "char", "address": "8" },
        { "dimension": "linecol", "address": "2:3" },
        {
          "dimension": "line", "address": "2",
          "errors": [
            {
              "message": "Malformed name at character 3: invalid character '*'", 
              "position": { "char": "3" }
            }
          ]
        }
      ]
    }
  ]
}
~~~

## Implementations

See [directory `examples`](examples) for an example implementation of an XML validator supporting this error format.

