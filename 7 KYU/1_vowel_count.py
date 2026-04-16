"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""



def get_count_v1(sentence: str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in sentence:
        if char in vowel:
            count += 1
    return count


def get_count_v2(sentence: str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    return sum(1 for char in sentence if char in vowel)


def get_count_v3(sentence: str):
    vowels = "aeiou"  # string works same as list for `in`
    return sum(c in vowels for c in sentence)