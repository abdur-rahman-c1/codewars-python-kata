"""
Description:

Given an array of integers your solution should find the smallest integer.

For example:

    Given [34, 15, 88, 2] your solution will return 2
    Given [34, -345, -1, 100] your solution will return -345

You can assume, for the purpose of this kata, that the supplied array will not be empty.

"""


def find_smallest_int(arr: list):
     arr.sort()
     return arr[0]

def find_smallest_int_v2(arr: list):
     return min(arr)

def find_smallest_int_v3(arr: list):
     fitered = sorted(arr)
     return fitered[0]