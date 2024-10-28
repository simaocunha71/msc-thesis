
def histogram(test):
    # Create an empty dictionary
    histogram = {}
    # Create a counter
    counter = 0
    # Iterate through the string and add each letter to the histogram dictionary if it's not there
    for letter in test:
        if letter not in histogram:
            histogram[letter] = 1
        else:
            histogram[letter] += 1
    # Create a list of tuples containing the letter and it's count
    histogram_list = []
    for key in histogram:
        histogram_list.append((key, histogram[key]))
    # Sort the list by the second element in the tuple
    histogram_list.sort(key = lambda x: x[1])
    # If there's only one element in the list, return the tuple
    if len(histogram_list) == 1:
        return histogram_list[0]
    # If there are more than one element in the list, return the last element
    else:
        return histogram_list[-1]

# Run tests
print(histogram('a b c')) # {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a')) # {'a': 2, 'b': 2}
print(histogram('a b c a b')) # {'a': 2, 'b': 2}
print(histogram('b b b b a')) # {'b': 4}
print(histogram('')) # {}
























































































































































