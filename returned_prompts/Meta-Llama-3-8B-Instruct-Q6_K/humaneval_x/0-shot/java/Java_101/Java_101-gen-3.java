Here is a simple solution in Java that uses the `split` method to split the input string into words and returns a list of those words:

```java
public List<String> wordStrings(String s) {
    String[] words = s.split("[,\\s]+");
    List<String> result = new ArrayList<>(Arrays.asList(words));
    return result;
}
```

In this solution, the `split` method is used to split the input string `s` into words. The regular expression `[,\\s]+` matches one or more commas or spaces. The resulting array of words is then converted to a list and returned.

This solution is case-sensitive and will treat punctuation marks as part of the words. If you want to ignore case and punctuation marks, you can use the following solution:

```java
public List<String> wordStrings(String s) {
    s = s.toLowerCase();
    s = s.replaceAll("[^a-z0-9\\s,]+", "");
    String[] words = s.split("[,\\s]+");
    List<String> result = new ArrayList<>(Arrays.asList(words));
    return result;
}
```

In this solution, the `toLowerCase` method is used to convert the input string to lowercase. The `replaceAll` method is used to remove all characters that are not letters, digits, spaces, or commas. The resulting array of words is then converted to a list and returned.