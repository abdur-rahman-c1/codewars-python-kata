"""
Description:

Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

"""

def bool_to_word_v1(boolean: bool):
    match(boolean):
        case True:
            return "Yes"
        case False:
            return "No"



def bool_to_word_v2(boolean: bool):
    return "Yes" if boolean else "No"


def bool_to_word_v3(boolean: bool):
    return {True: "Yes", False: "No"}[boolean]

def bool_to_word_v4(boolean: bool):
    return ["No", "Yes"][boolean]