# Summary

- After running the coverage function the first time, I got a coverage of 90% with 4 misses out of 42 statements, 2/20 on order_io.py and 2/22 on pricing.py

## Uncovered lines or functions

- I was missing lines 12 and 15 from order_io.py and lines 20 and 25 from pricing.py
- Three of the missing lines were raising exceptions and the last one was a continue line

## Acceptable uncovered lines or functions

- I think the continue line being missing is acceptable because there's not really a need or a good way to test whether the continue block is working properly
- The raised exception lines should be covered because those are edge cases that we need to be able to handle and make sure that they are caught properly

# After improvement

- After improvement, I got 98% coverage, only missing the continue line in order_io.py
- I added a test for all the edge cases that would raise the various exceptions previously unchecked
