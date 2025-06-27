# Locator languages

This memo introduces a specific class of formal languages used to identify elements in a digital document. These languages can be called **locator languages** with **locators** as instances of these languages.

A simple examples are 

- line numbers
- POSIX Path

Many locator languages are informally specified and/or constraint or they are a subset of 

**locators**.

**locator languages** summarized ideas around 

# Locating in digital documents

For referring to specific parts of a document

Use cases: Hypertext/Hyperdata, error location...

## Nested document models

CSV embedded in an XML envelope in an gzipped XML file that is in a TAR archive

- POSIX Path and optional number (tar allows for multiple files with same name)
- unzip
- XPath
- Cell

~~~
file  = "path/of/file"          => list of files
index = 0                       => first file
xpath = "/xml/element/path"     => nodeset
line  = 3"                      => character sequence
~~~

Is there a subset of XPath [Path Expressions](https://www.w3.org/TR/xpath-31/#id-path-expressions) to reference elements?

## Open Questions

Locators to single object vs. locator to sets of objects. Example:

`char=3-7`, vs. `char=3-7,8-9`

## References

"Multimedia Segments" introduced by Will, Bernstein, and Rosetto (2024) to reference segments of multimedia documents.

- <https://www.nutrient.io/guides/web/annotations/introduction-to-annotations/what-are-annotations/#the-pdf-annotation-model>
- Unified Multimedia Segmentation - A Comprehensive Model for URI-based Media Segment Representation <https://doi.org/10.4230/TGDK.2.3.1>
