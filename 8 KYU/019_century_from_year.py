"""
Introduction

The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
Task

Given a year, return the century it is in.
Examples

1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28

Note: this kata uses strict construction as shown in the description and the examples, you can read more about it here
https://en.wikipedia.org/wiki/Century
"""

def century_v1(year): # Intital version
    century = year // 100
    if year % 100 != 0:
        century += 1
    return century

def century_v2(year): 
    return (year + 99) // 100

"""
V2 Visualised:
Year 1700 (exact):
  1700 + 99 = 1799
  1799 // 100 = 17 ✓ (stays in 17th century)

Year 1705 (has leftover):
  1705 + 99 = 1804
  1804 // 100 = 18 ✓ (pushed to 18th century!) 
"""