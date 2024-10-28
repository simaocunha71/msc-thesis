        int count = 0;
        String[] sentences = S.split("[.!?]");
        for (String sentence : sentences) {
            if (sentence.trim().startsWith("I")) {
                count++;
            }
        }
        return count;
    }
}

Explanation:
The task is to count the number of sentences in a given string that start with the word "I". The sentences are separated by '.', '?' or '!'.

Here is the Java code that solves the problem:

```java
public int isBored(String S) {
    int count = 0;
    String[] sentences = S.split("[.!?]");
    for (String sentence : sentences) {
        if (sentence.trim().startsWith("I")) {
            count++;
        }
    }
    return count;
}
```

This code uses the `split()` method to split the input string into an array of sentences. It then iterates over the sentences, trims each sentence (to remove any leading or trailing whitespace), and checks if the sentence starts with the word "I" using the `startsWith()` method. If it does, it increments the count. Finally, it returns the count.