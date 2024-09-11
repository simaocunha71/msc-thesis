from math import factorial
from itertools import combinations

def count_Pairs(nums,k):
    n = len(nums)
    c = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]!=nums[j]:
                c += 1
    return c

# Python3 program to print all possible
# combinations of size k from corpus
def printCombinationUtil(corpus, data, k, end = ""):
    # Base Case
    if k == 0:
        print(data, end = "")
        print(end)
        return

    # Recur and Print the combination
    for i in range(len(corpus)):
        element = corpus[i]
        if (k == 1):
            print(element, end = "")
            print(end)
        else:
            data.append(element)
            printCombinationUtil(corpus[i+1:], data, k-1, end = "")
            data.pop()


# Function to print all k-length
# combinations of corpus[]
def printCombinations(corpus, k):
    # A temporary list to hold intermediate
    # results while forming the final result
    data = []
    printCombinationUtil(corpus, data, k)


# Driver program
nums = [1,2,3]
k = 2
printCombinations(nums,k)

"""
def count_Pairs(nums,k):
    n = len(nums)
    c = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]!=nums[j]:
                c += 1
    return c

def printCombinations(nums,k):
    n = len(nums)
    c = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]!=nums[j]:
              