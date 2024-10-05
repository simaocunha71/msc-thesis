
def words_in_sentence(sentence):
    sentence = sentence.split(" ")
    result = ""
    for word in sentence:
        if len(word) in [2, 3, 5, 7]:
            result += word + " "
    return result.strip()




```
```

```

```

```

```

```
```

# Solution

To solve the problem, we need to follow these steps:

1. Split the sentence into a list of words by using the `split()` function and passing the space character as the delimiter.
2. Initialize an empty string variable called `result` to store the words whose lengths are prime numbers.
3. Iterate over each word in the `sentence` list.
4. Check if the length of the current word is a prime number by using a conditional statement. We can do this by checking if the length is in the list of prime numbers `[2, 3, 5, 7]`.
5. If the length of the current word is a prime number, append the word to the `result` string and add a space character after it.
6. After iterating over all the words in the `sentence` list, return the `result` string.

Here's the code that implements the above steps:

```python
def words_in_sentence(sentence):
    sentence = sentence.split(" ")
    result = ""
    for word in sentence:
        if len(word) in [2, 3, 5, 7]:
            result += word + " "
    return result.strip()
```

This function takes a string `sentence` as input and returns a string `result` that contains the words from the original sentence, whose lengths are prime numbers, in the same order as the original sentence.

For example, if we call the function with the input `"This is a test"`, it will return `"is"` because the length of the word `"is"` is 2, which is a prime number.

Similarly, if we call the function with the input `"lets go for swimming"`, it will return `"go for"` because the lengths of the