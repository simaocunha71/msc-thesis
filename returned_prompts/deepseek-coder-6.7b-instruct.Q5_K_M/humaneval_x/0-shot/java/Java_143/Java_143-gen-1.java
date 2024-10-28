        StringBuilder result = new StringBuilder();
        String[] words = sentence.split(" ");
        for (String word : words) {
            if (isPrime(word.length())) {
                result.append(word).append(" ");
            }
        }
        // Remove the trailing space
        if (result.length() > 0) {
            result.setLength(result.length() - 1);
        }
        return result.toString();
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```


## Solution:

This problem can be solved by using the string manipulation and number theory.

The string is split into words by spaces, and for each word the length is checked if it is a prime number. If it is, the word is appended to the result string.

The method isPrime is used to check if a number is prime. It returns false if the number is less than or equal to 1, or if it is divisible by any number up to its square root. If it is not divisible by any of these numbers, it is a prime number.

Finally, the trailing space is removed from the result string if it exists and the string is returned.

The time complexity is O(n*m), where n is the number of words in the sentence and m is the average length of the words. The space complexity is O(n), as a new string is created to store the result.

This solution satisfies the given constraints as the length of the sentence and words is within the range of 1 to 100, and the sentence contains only letters.

This solution is efficient and works well for this problem.

## Test cases:

```java
Solution solution = new Solution();

// Test case 1
assert "is".equals(solution.wordsInSentence("This is a test"));

// Test case 2
assert "go for".equals(solution.wordsInSentence("