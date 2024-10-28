```java
public String antiShuffle(String s) {
    String[] words = s.split(" ");
    StringBuilder result = new StringBuilder();
    for (String word : words) {
        char[] chars = word.toCharArray();
        Arrays.sort(chars);
        result.append(new String(chars)).append(" ");
    }
    return result.toString().trim();
}
```

Explanation:
The problem is asking to create a function that takes a string as an input and returns a new string where all the words in the input string are replaced by a new word where all the characters are arranged in ascending order based on ASCII values. The order of words and blank spaces in the sentence should be maintained.

We can solve this problem by splitting the input string into words, sorting the characters in each word and then joining them back together. We also need to trim the resulting string to remove any extra spaces.

Here is the Java code that solves this problem:

```java
public String antiShuffle(String s) {
    String[] words = s.split(" ");
    StringBuilder result = new StringBuilder();
    for (String word : words) {
        char[] chars = word.toCharArray();
        Arrays.sort(chars);
        result.append(new String(chars)).append(" ");
    }
    return result.toString().trim();
}
```

In this code, we first split the input string into words using the `split` method with a space character as the delimiter. Then we create a `StringBuilder` object to build the resulting string. We iterate over each word, sort its characters using the `Arrays.sort` method, convert the sorted characters back to a string using the `String` constructor, and append it to the `StringBuilder`. Finally, we append a space character to the `StringBuilder` to separate the words. After iterating over all words, we return the resulting string by calling the `toString` method on the `StringBuilder` object and trimming any extra spaces using the `trim` method.