You can solve this problem in Java by using the `split()` method of the `String` class. Here is the Java code:

```java
public Object splitWords(String txt) {
    // split on whitespace
    String[] words = txt.split("\\s+");
    if (words.length > 1) {
        return Arrays.asList(words);
    }
    // split on commas
    words = txt.split(",");
    if (words.length > 1) {
        return Arrays.asList(words);
    }
    // count lower-case letters with odd order in the alphabet
    int count = 0;
    for (char c : txt.toCharArray()) {
        if (Character.isLowerCase(c) && (c - 'a') % 2 != 0) {
            count++;
        }
    }
    return count;
}
```
In this code, the `split()` method is used to split the input string `txt` into an array of words. The regular expression `\\s+` matches one or more whitespace characters, and `","` matches a comma. If the resulting array has more than one element, it means that the string was split on whitespace or commas, so the code returns it as a `List<String>`.

If the resulting array has one or zero elements, it means that the string was not split on whitespace or commas, so the code counts the lower-case letters with odd order in the alphabet. It does this by iterating over the characters in the string, checking if each character is a lower-case letter and if its order in the alphabet is odd, and incrementing a counter for each such letter.

The method then returns the count of such letters.