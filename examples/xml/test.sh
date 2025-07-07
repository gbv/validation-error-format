#!/bin/bash

# Test Anything Protocol (TAP)
start_testing() { TEST_COUNTER=0; }
done_testing() { echo 1..$TEST_COUNTER; }
ok() { TEST_COUNTER=$(($TEST_COUNTER+1)); echo ok $TEST_COUNTER - $@; }
not_ok() { TEST_COUNTER=$(($TEST_COUNTER+1)); echo not ok $TEST_COUNTER - $@; }
diag() { awk '{print "#",$0}'; }

# Messages may differ between library versions so remove them when comparing
normalize() { jq -S 'walk(if (type == "object" and .message) then del(.message) else . end)'; }

validate() {
    expect=$1
    shift

    got=got.tmp
    want=want.tmp
    normalize < $expect > $want
    
    ./validate-xml "$@" | normalize > $got
    if diff -Bb $got $want > /dev/null; then
        ok "./validate-xml $@"
    else
        not_ok "./validate-xml $@"
        diff -Bn $got $want | diag
    fi
}

start_testing

validate test/malformed.json        malformed.xml
validate test/malformed.json        -s schema.xsd malformed.xml
validate test/ok.json               invalid.xml
validate test/invalid.json          -s schema.xsd invalid.xml

# TODO: test input from STDIN

done_testing
