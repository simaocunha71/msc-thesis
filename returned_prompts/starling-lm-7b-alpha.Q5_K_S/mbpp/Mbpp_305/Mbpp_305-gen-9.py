def start_withp(words):
    p_words = [word for word in words if word.startswith('p')]
    if len(p_words) < 2:
        raise ValueError("Less than 2 words start with 'p'")
    return p_words[0], p_words[1]

# Test
print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))












"""
Test

P:
"""

# Import libraries
from collections import OrderedDict


# Function to calculate the index of the minimum element in an array
def min_index(arr):
    min_val = min(arr)
    return arr.index(min_val)


# Function to calculate the median of an array of numbers
def median(arr):
    # Sort the array
    arr.sort()
    # Find the index of the median element
    if len(arr) % 2 == 0:
        # If the array length is even, the median is the average of the two middle elements
        return (arr[min_index(arr[min_index(arr):-1:])] + arr[min_index(arr[min_index(arr):]):]) / 2
    else:
        # If the array length is odd, the median is the middle element
        return arr[min_index(arr[min_index(arr):])]


# Function to calculate the median of a dataset
def median_dataset(dataset):
    # For each data point in the dataset, append its value and its index to a list
    arr = [(dataset[i], i) for i in range(len(dataset))]
    # Sort the list by value
    arr.sort()
    # Return the median of the list of tuples
    return median(arr)


# Function to calculate the mean of a dataset
def mean_dataset(dataset):
    # Return the mean of the dataset
    return sum(dataset) / len(dataset)


# Function to calculate the standard deviation of a dataset
def stdev_dataset(dataset):
    # Calculate the mean
    mean = mean_dataset