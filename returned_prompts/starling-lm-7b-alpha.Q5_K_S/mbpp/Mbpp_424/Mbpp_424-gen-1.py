def extract_rear(tup):
    return [i[-1] for i in tup]


# assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']


# Python 3 program to print all
# permutations of a string

from itertools import permutations

str = 'ABC'
# Function to print all permutations
# of string
def find_permutation(str):
    # Generating all permutations
    # of the given string
    perms = permutations(str)
    for perm in perms:
        print("".join(perm))

# Driver code
if __name__ == "__main__":
    find_permutation(str)


# Python program to find the first common element
# between two lists

# Function to find first common element
def find_common(list1, list2):
    list1.sort()
    list2.sort()
    i = 0
    while i < len(list1):
        if list1[i] in list2:
            return list1[i]
        i += 1
    return -1

# Driver Program
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(find_common(list1, list2))


# Python program to find the maximum number
# of coins, such that the sum of coins is
# equal to the given number.

# Function to return the maximum number
# of coins
def coins(m):
    # Initialize result
    result = 0

    # Traverse through all denominations
    for i in range(1, 100):
        # While the number is greater than 0 and there
        # is a coin for the current denomination
        while (m >= i):
            # Update the number and the result
            m = m - i
            result = result + 1

    return result

# Driver Program
if __name__ == "__main__":
    m = 15
    print(coins(