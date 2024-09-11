"""
def max_occurrences(list):
    occurrences = {}
    for item in list:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    max_item = None
    max_occurrence = 0
    for key, value in occurrences.items():
        if value > max_occurrence:
            max_item = key
            max_occurrence = value
    return max_item

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))
"""

# Python3 program to count
# frequency of elements
# in an array

# Function to count frequency
# of all elements in a given
# array
def countFrequency(arr, n):

    # Create an empty dictionary
    # to store count of all
    # elements
    count = dict()

    # Traverse through all elements
    # of the array
    for i in range(n):

        # If element is already
        # present in dictionary
        # increase its count by 1
        if arr[i] in count:
            count[arr[i]] += 1

        # Else insert the element
        # in dictionary with value 1
        else:
            count[arr[i]] = 1

    # To get maximum occurring
    # element from dictionary
    max_item = None
    max_occurrence = 0
    for key, value in count.items():
        if value > max_occurrence:
            max_item = key
            max_occurrence = value

    return max_item

# Driver code
if __name__ == "__main__":
    arr = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]
    n = len(arr)
    print(countFrequency(arr, n))

