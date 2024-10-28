The problem is asking to filter the words in a given sentence that have lengths which are prime numbers, and return these words as a string. The order of the words in the returned string should be the same as in the original sentence.

Here's a solution in Java:

```java
public String wordsInSentence(String sentence) {
    String[] words = sentence.split(" ");
    StringBuilder result = new StringBuilder();
    for (String word : words) {
        if (isPrime(word.length())) {
            result.append(word).append(" ");
        }
    }
    return result.toString().trim();
}

public boolean isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
```

In this solution, we first split the input sentence into words using the `split` method. Then, we iterate over each word and check if its length is a prime number using the `isPrime` method. If it is, we append the word to the result string builder. Finally, we return the result string after trimming any trailing spaces.

The `isPrime` method checks if a given number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, the number is not prime and we return `false`. Otherwise, the number is prime and we return `true`.