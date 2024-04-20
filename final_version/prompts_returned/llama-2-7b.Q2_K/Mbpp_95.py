"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""

def Find_Min_Length(listOfLists):
    minLength = len(sys.argv) + 1
    i = 0
    print(i)
    if (len(listOfLists) > 0 and listOfLists[0] != []):
        # if the input list is not empty we use recursion to find our answer
        minLength = Find_Min_Length([listOfLists[0]])
    elif (len(listOfLists) == 0 or len(listOfLists[0]) < minLength + 1):
        # if the list is empty, we simply return the index of our python program
        print("The smallest length in a list is " + str(i))
    else:
        # otherwise, use iteration to find the minimum
        size = (len(listOfLists[0]) + 1)
        i += 1
        minLength = len(sys.argv) + 1
        print("The smallest length in a list is " + str(i))
    return minLength
