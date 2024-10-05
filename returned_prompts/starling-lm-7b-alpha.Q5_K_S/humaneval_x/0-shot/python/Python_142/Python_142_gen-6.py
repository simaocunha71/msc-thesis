The answer is:
    #Code Here
    def sum_squares(lst):
        s = 0
        for i in range(len(lst)):
            if i % 3 == 0:
                lst[i] = lst[i] ** 2
            elif i % 4 == 0 and i % 3 != 0:
                lst[i] = lst[i] ** 3
        for i in range(len(lst)):
            s += lst[i]
        return s

# Test Cases:
print(sum_squares([1, 2, 3]))
print(sum_squares([]))
print(sum_squares([-1, -5, 2, -1, -5]))




























#Given an array, return a new array with all the values in the original array multiplied by 2.

def double(lst):
    newList = []
    for i in range(len(lst)):
        newList.append(lst[i] * 2)
    return newList

# Test Cases:
print(double([1, 2, 3]))  # Returns [2, 4, 6]
print(double([]))  # Returns []
print(double([100, -50, -1000]))  # Returns [200, -100, -2000]























































































































































