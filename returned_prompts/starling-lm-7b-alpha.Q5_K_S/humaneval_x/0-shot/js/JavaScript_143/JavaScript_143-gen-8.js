To solve this problem, we can follow these steps:

1. Split the given sentence into an array of words using the `split()` method, with a space as the separator.
2. Define a function called `isPrime` that takes a number as input and returns `true` if the number is prime, and `false` otherwise. This function will be used to check if a word's length is a prime number.
3. Use the `filter()` method on the `words` array to create a new array called `filteredWords` that contains only the words whose lengths are prime numbers. The `filter()` method applies the `isPrime` function to each word's length and returns a boolean value. If the boolean value is `true`, the word is included in the `filteredWords` array.
4. Finally, use the `join()` method on the `filteredWords` array to convert it back into a string, with each word separated by a space.
5. Return the resulting string.

The time complexity of this solution is O(n), where n is the number of words in the sentence, as we