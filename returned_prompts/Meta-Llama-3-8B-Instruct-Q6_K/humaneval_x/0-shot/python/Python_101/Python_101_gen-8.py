    # Split the string into words and return an array of the words.
    # The string can be separated by commas or spaces.
    def words_string(s):
        return s.replace(",", " ").split()

    # Test the function
    print(words_string("Hi, my name is John"))  # Output: ['Hi', 'my', 'name', 'is', 'John']
    print(words_string("One, two, three, four, five, six"))  # Output: ['One', 'two', 'three', 'four', 'five', 'six']  # Output: ['One', 'two', 'three', 'four', 'five', 'six']



Solution:
    # Split the string into words and return an array of the words.
    # The string can be separated by commas or spaces.
    def words_string(s):
        return s.replace(",", " ").split()

    # Test the function
    print(words_string("Hi, my name is John"))  # Output: ['Hi', 'my', 'name', 'is', 'John']
    print(words_string("One, two, three, four, five, six"))  # Output: ['One', 'two', 'three', 'four', 'five', 'six']



This function works by first replacing all commas in the string with spaces. This allows the string to be split on both commas and spaces, effectively splitting it into individual words. The split() function is then called on the resulting string, which splits it into a list of words. This list is then returned as the result.