    The provided solution works by first splitting the input sentence into an array of words. Then, it checks if the length of each word is a prime number by invoking the `isPrime` method. If the length of a word is prime, it's appended to a `StringBuilder` object. Finally, the `toString` method of `StringBuilder` is called to get the final string.

    The `isPrime` method works by checking if a number is prime. If the number is less than or equal to 1, it returns `false`. If not, it checks if the number is divisible by any integer from 2 to the square root of the number. If it is divisible, it returns `false`. If it is not divisible by any of these numbers, it returns `true`, indicating that the number is prime.

    The time complexity of the solution is O(n*m), where n is the number of words in the sentence and m is the average length of the words. This is because for each word, we are checking if the length of the word is prime which takes O(m) time, and we are doing this for n words.

    The space complexity of the solution is O(n), as we are storing the words in an array and the prime words in a `StringBuilder` object.

    Note: The `trim` method is used to remove any trailing spaces from the final string.

    This solution assumes that the sentence only contains letters and spaces, as mentioned in the problem constraints. If the sentence contains other characters, the `isPrime