

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """

    if type(lst) is not list:
        return "You entered an empty list."

    total_square = 0
    counter = len(lst) - 1
    for i in range(counter, 0, -1):
        if lst[i] % 2 == 1:
            continue

        temp = (abs(int(lst[i])**2))
        total_square += int(temp ** 2)
        
    return "Sum of Squared Numbers are {0}".format(total_square)

sum_squares([1,4,9]) # output : Sum of Squared Numbers are 98
