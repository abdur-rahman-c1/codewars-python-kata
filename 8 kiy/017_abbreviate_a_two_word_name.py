"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""

def abbrev_name_v1(name):
    split = name.split(" ")
    result = []
    for i in split:
        result.append(i[0])
    final = ".".join(result)
    return final

def abbrev_name_v2(name):
    return ".".join(item[0] for item in name.split())


def abbrev_name_v3(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"