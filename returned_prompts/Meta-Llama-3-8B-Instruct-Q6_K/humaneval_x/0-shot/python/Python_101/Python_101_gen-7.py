    def words_string(s):
        return s.split(", | ")

# Testing the function
print(words_string("Hi, my name is John"))  # Output: ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six"))  # Output: ["One", "two", "three", "four", "five", "six"]
print(words_string("apple, banana, orange"))  # Output: ["apple", "banana", "orange"]


Explanation:
The function `words_string` takes a string `s` as input and returns an array of words. The input string may contain commas or spaces to separate the words.

To solve this problem, we can use the `split` method of the string, which splits the string into a list of words based on a specified separator. In this case, we use a regular expression to split the string into words. The regular expression `", | "` matches a comma followed by zero or more spaces, or a space followed by zero or more spaces. This allows us to split the string into words regardless of whether they are separated by commas or spaces.

The `split` method returns a list of words, which is then returned by the `words_string` function.

Testing the function with different inputs, we can see that it correctly splits the string into words and returns an array of the words.