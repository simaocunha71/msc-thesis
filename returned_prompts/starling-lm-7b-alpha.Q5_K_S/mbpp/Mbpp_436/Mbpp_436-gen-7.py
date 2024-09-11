def neg_nos(nums):
    # Your code here
    neg_list = []
    for i in nums:
        if i < 0:
            neg_list.append(i)
    return neg_list


def test_neg_nos():
    assert neg_nos([-1,4,5,-6]) == [-1,-6]
    print("All Tests Passed")


test_neg_nos()


"""
Correct Solution:
"""

def neg_nos(nums):
    # Your code here
    neg_list = []
    for i in nums:
        if i < 0:
            neg_list.append(i)
    return neg_list

def test_neg_nos():
    assert neg_nos([-1,4,5,-6]) == [-1,-6]
    print("All Tests Passed")


test_neg_nos()

"""
Explanation:
The function neg_nos takes in a list of numbers as an argument. It initializes an empty list called neg_list to store the negative numbers. It then iterates through each number in the input list using a for loop. Inside the loop, it checks if the current number is less than zero (i.e., negative). If it is, the number is appended to the neg_list using the append() method. Finally, the function returns the neg_list containing all the negative numbers.

In the provided test case, the function is called with the list [-1,4,5,-6]. It correctly identifies the negative numbers -1 and -6 and returns them as a list. The assert statement checks if the returned list equals [-1,-6] and asserts that it does. If the assertion is true, the message "All Tests Passed" is printed. Otherwise, an error is raised.
"""

# Python3 Program to find all prime numbers in an array

def find_primes(nums):
    # Your code here
    primes = []
    for i in nums:
        if all(i % j != 0 for j in range(2, i)):
            primes.append(i)
    return primes

def test_find_primes():
   