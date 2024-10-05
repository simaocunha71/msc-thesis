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
The function takes a string `s` as input and returns an ordered version of it. It first splits the string into words using the `split` method. Then, for each word, it converts the word into a character array, sorts the array using the `sort` method, and creates a new string from the sorted array. The resulting string is appended to the `result` `StringBuilder`. Finally, the function returns the `result` string, but before that, it trims the string to remove the trailing space.

The time complexity of this function is O(n*m*log(m)), where n is the number of words in the input string and m is the maximum length of a word. This is because the `sort` method has a time complexity of O(m*log(m)) and it is called for each word. The space complexity is O(n*m), where n is the number of words in the input string and m is the maximum length of a word. This is because the `result` `StringBuilder` stores the sorted strings.