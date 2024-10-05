    # Initialize an empty list to store the words
    words = []

    # Split the string into words using either commas or spaces as delimiters
    for word in s.replace(",", " ").split():
        # Add each word to the list
        words.append(word)

    # Return the list of words
    return words
print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))


Output:
['Hi', 'my', 'name', 'is', 'John']
['One', 'two', 'three', 'four', 'five', 'six']



Explanation:
The function words_string takes a string of words separated by commas or spaces as input. It splits the string into words using the replace method to replace commas with spaces and then the split method to split the string into words. It then iterates over the list of words, adding each word to a new list. Finally, it returns the list of words. The function is tested with two examples, "Hi, my name is John" and "One, two, three, four, five, six", and the output is a list of the words in each string.