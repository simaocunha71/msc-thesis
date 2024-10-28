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

private boolean isPrime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}
```
Explanation:
The problem asks you to return a string containing only the words from the original sentence whose lengths are prime numbers. The order of the words in the new string should be the same as the original one.

In the code above, we first split the input sentence into words using the `split` method with a space character as the delimiter. Then we iterate over each word and check if its length is a prime number using the `isPrime` method.

If a word's length is prime, we append it to the `result` string builder. Finally, we return the `result` string after trimming any trailing spaces.

The `isPrime` method checks if a given number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, the number is not prime, and we return `false`. If the number is not divisible by any of these values, it is prime, and we return `true`.