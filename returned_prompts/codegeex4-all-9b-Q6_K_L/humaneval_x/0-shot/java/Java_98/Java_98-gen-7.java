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

Explanation:
The function `countUpper` takes a string `s` as input and counts the number of uppercase vowels in even indices. The function iterates over the string `s` with a step of 2, checking if the character at each index is an uppercase vowel. If it is, the count is incremented. Finally, the function returns the count.