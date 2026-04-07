"""
Description:

We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?
Examples (input --> output):

123  --> "123"
999  --> "999"
-100 --> "-100"



"""
# Solution 1
def number_to_string(num):
    return str(num)

# Solution 2
def number_to_string(num):
    return f"{num}"


print(number_to_string(55))