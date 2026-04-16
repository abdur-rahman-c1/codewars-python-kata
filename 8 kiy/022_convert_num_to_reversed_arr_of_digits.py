"""
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
Example (Input => Output):

35231 => [1,3,2,5,3]
0     => [0]

"""

def digitize(n):
    string = str(n)
    digits = list(string)            
    reversed_digits = digits[::-1]      
    return [int(d) for d in reversed_digits]  