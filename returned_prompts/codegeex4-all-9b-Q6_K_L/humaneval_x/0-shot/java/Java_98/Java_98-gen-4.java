Here is a solution that uses the Java String class's methods to count the number of uppercase vowels in even indices:

```java
public int countUpper(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i += 2) {
        char c = s.charAt(i);
        if (Character.isUpperCase(c) && "AEIOU".indexOf(c) != -1) {
            count++;
        }
    }
    return count;
}
```

This method iterates over every even index of the string, checks if the character at that index is an uppercase vowel (by checking if it is in the string "AEIOU"), and if so, increments the count. The method returns the final count after iterating over all the characters.