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
We split the input string into words using the `split` method. Then, for each word, we convert it to a character array, sort it using the `Arrays.sort` method, and create a new string from the sorted array using the `String` constructor. We append this new string to our result `StringBuilder` and add a space character to separate it from the next word. Finally, we return the result `StringBuilder` as a string and trim any trailing spaces using the `trim` method.