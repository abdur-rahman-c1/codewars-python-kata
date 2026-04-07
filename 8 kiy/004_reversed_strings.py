"""
Description:

Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'


"""

# solution 1:
def solution1(string: str):
    return string[::-1]  # uses string slice while keeping everything at default including start and stop. only the step is told to be in a reverse order. 

# solution 2:
def solution2(string: str):
    return ''.join(reversed(string))

# reversed returns an iterator version of the given string in reverse order
# it essentially is like vending machine where string are sorted and spits out one string after another. you can't see it, it's hidden inside of ram storage
# ''.join catches all spitted out strings and joins them together

