#!/usr/bin/env python

import xml.etree.ElementTree as ET
import xmlschema
import json
import sys
import argparse

parser = argparse.ArgumentParser("validate-xsd")
parser.add_argument("schema", help="XML Schema file", type=str)
parser.add_argument("file", help="XML file", nargs='*', type=str, default=["-"])
args = parser.parse_args()

schema = xmlschema.XMLSchema(args.schema)

# for debugging
def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))

def validate(file):
    try:
        tree = ET.parse(file)
    except ET.ParseError as e:
        line, col = e.position
        error = {
            "message": str(e),
            "type": [f"expat-error-code:{e.code}"],
            "position": {
                "line": line,
            }
        }
        if col > 0:
            error["position"]["linecol"] = f"{line}:{col}"
        print(json.dumps(error))
        return

    for e in schema.iter_errors(tree):
        error = {
          "message": e.reason
        }
        if e.path is not None:
            error["position"] = { "xpath": e.path }
        print(json.dumps(error))

for file in args.file:
    validate(sys.stdin if file == "-" else file)

