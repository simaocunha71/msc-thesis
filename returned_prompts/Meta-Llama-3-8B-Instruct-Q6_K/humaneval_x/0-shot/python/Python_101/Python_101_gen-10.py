    def words_string(s):
        # Remove commas and spaces from the string
        s = s.replace(",", "").replace(" ", "")
        
        # Split the string into words
        words = s.split()
        
        # Return the array of words
        return words

# Test the function
print(words_string("Hi, my name is John"))  # Output: ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six"))  # Output: ["One", "two", "three", "four", "five", "six"]


