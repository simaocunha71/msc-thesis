Explanation:
The problem is asking to filter out the words from the sentence which have prime length. We first split the sentence into words using the `strings.Split` function. Then we iterate over each word and check if its length is prime using the `isPrime` function. If the length is prime, we add the word to the result string. Finally, we return the result string after trimming the trailing space.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is divisible, the number is not prime and we return `false`. If the number is not divisible by any of these values, it is prime and we return `true`.

The time complexity of this solution is O(n*m) where n is the number of words in the sentence and m is the maximum length of a word. The space complexity is O(n) for the result string.