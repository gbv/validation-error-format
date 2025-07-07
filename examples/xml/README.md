# XML Validator emitting Data Validation Error Format

This directory contains a Python implementation of a validator for XML documents. It supports XML Schema to validate against.

## Requirements and installation

The script requires Python >= 3.3.

Install dependencies listed in `requirements.txt` with `python -mvenv .venv && . .venv/bin/activate` (or just call `make`).

## Usage

Call `./validate-xml --help` for usage help.

~~~sh
./validate-xml -s schema.xsd file.xml
~~~

## Tests

Unit tests of the script can be executed with script `./tests.sh` (or just call `make test`). Requires `jq` to be installed).
