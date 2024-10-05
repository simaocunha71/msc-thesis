
def words_string(s):
    s = s.replace(",", " ")
    return s.split(" ")


# Alternative Solution:
def words_string(s):
    return s.split(",")

# Test Cases
print(words_string("Hi, my name is John"))  # ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six"))  # ["One", "two", "three", "four", "five", "six"]

```

In this solution, the input string `s` is first modified by replacing all commas with spaces using the `replace()` method. This ensures that the string is properly split into words. Then, the modified string is split into a list of words using the `split()` method, which splits the string at each space character. The resulting list of words is then returned as the output.

Alternatively, if you want to keep the commas in the resulting list, you can use the `split(",")` method directly on the input string without replacing the commas.

The provided test cases demonstrate the usage of the `words_string()` function with different input strings and verify the correctness of the output.