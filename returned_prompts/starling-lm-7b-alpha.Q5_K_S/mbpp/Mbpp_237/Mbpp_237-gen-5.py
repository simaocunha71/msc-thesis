def check_occurences(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d




"""
"""

# Python3 program to count frequency of
# elements in an array.

# Function to count frequency of
# elements in an array
def countFreq(arr):
    # Create an empty dictionary
    # to store frequency of elements
    freq = {}

    # Traverse through the given array
    for i in range(len(arr)):

        # If element is already present
        # in dictionary, increase its
        # value by 1. Else, insert
        # the element in dictionary
        # with frequency as 1
        if (arr[i] in freq):
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    # Returns frequency of all
    # elements in the array
    return freq



# Driver program
arr = [3, 1, 1, 3, 2, 5, 5, 2, 6, 3]

# Function call
freq = countFreq(arr)

# Print the frequency of all
# elements in the array
for i in freq:
    print(i, "->", freq[i])




# Python3 program to count frequency of
# elements in an array.

# Function to count frequency of
# elements in an array
def countFreq(arr):
    # Create an empty dictionary
    # to store frequency of elements
    freq = {}

    # Traverse through the given array
    for i in range(len(arr)):

        # If element is already present
        # in dictionary, increase its
        # value by 1. Else, insert
        # the element in dictionary
        # with frequency as 1
        if (arr[i] in freq):
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    # Returns frequency of all
    #