"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""

def move_num(s):
    """
    :param s: string or list of strings
    :return: List of strings.
     """
    if type(s) is str:
        return [move_num(x) for x in s.split()]
    elif type(s) is not list:
        print("You have to put a string or a list")
        exit(1)
    res = []
    for i, word in enumerate(s):
        if int(word[:-1]) > 0 and int(word[:-1]) < 20:
            s[i] = word + str(int(word[:-1]))
            res.append(s[i])
    return res
