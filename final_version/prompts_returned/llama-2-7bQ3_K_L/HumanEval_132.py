
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''

    string = str(string)
    # print("'", str(string), "'")
    counter = 0

    while len(string.split()) > 1:
        # print("'", str(string), "'")
        try:
            if (len(string[counter].find(']')) == 2):
                counter += 1
        except:
            pass
    
    return True if len(string.split()) > 1 else False

def get_nested_levels(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return a list of all possible nested levels in the string.
    
    get_nested_levels('[[]]') ➞ [0,1]
    get_nested_levels('][]][[]']') ➞ [2,3]
    get_nested_levels('[]][]][[][][][]']') ➞ []
    '''

    string = str(string)
    
    counter = 0
    nested_levels_list = [str(counter)]
    # print("'", str(string), "'")

    while len(string.split()) > 1:
        # print("'", str(string), "'")
        try:
            if (len(string[counter].find(']')) == 2):
                counter += 1
        except:
            pass
            
        nested_levels_list.