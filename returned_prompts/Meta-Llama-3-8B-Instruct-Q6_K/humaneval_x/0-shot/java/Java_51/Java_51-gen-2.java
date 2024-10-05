Here is the solution:
```java
public String removeVowels(String text) {
    StringBuilder result = new StringBuilder();
    for (char c : text.toCharArray()) {
        if (!"aeiouAEIOU".indexOf(c) != -1) {
            result.append(c);
        }
    }
    return result.toString();
}
```
Explanation:
This function iterates over each character in the input string. If the character is not a vowel (i.e., its index in the string "aeiouAEIOU" is not -1), it is appended to the result string. The function returns the resulting string.

Note that we use a StringBuilder to build the result string, which is more efficient than concatenating strings using the + operator. We also use the toCharArray() method to convert the input string to a character array, which is more efficient than iterating over the string using a for-each loop.