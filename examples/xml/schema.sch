<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://www.ascc.net/xml/schematron">
  <sch:pattern name="Check structure">
    <sch:rule context="a">
      <sch:assert test="@id">The element a must have an id</sch:assert>
    </sch:rule>
  </sch:rule>
</sch:schema>
