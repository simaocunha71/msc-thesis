Here is a Java solution to the problem:

```java
public String getClosestVowel(String word) {
    for (int i = word.length() - 2; i > 0; i--) {
        char c = word.charAt(i);
        if ("AEIOUaeiou".indexOf(c) != -1 && "AEIOUaeiou".indexOf(word.charAt(i - 1)) == -1
                && "AEIOUaeiou".indexOf(word.charAt(i + 1)) == -1) {
            return String.valueOf(c);
        }
    }
    return "";
}
```
This solution works by iterating through the string from right to left (excluding the first and last characters) and checking if the current character is a vowel and the adjacent characters are not vowels. If such a character is found, it is returned. If no such character is found, an empty string is returned.