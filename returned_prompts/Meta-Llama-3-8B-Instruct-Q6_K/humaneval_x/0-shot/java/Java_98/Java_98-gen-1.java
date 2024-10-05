Here is a Java solution for the problem:

```java
public int countUpper(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i % 2 == 0 && s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') {
            count++;
        }
    }
    return count;
}
```

This solution iterates over the input string `s` and checks each character's index. If the index is even (`i % 2 == 0`) and the character is an uppercase vowel (`s.charAt(i) >= 'A' && s.charAt(i) <= 'Z'`), it increments the `count` variable. Finally, it returns the `count` variable. 

For example, if the input string is "aBCdEf", the function will return 1 because there is one uppercase vowel ('B') at an even index. If the input string is "abcdefg", the function will return 0 because there are no uppercase vowels at even indices. If the input string is "dBBE", the function will return 0 because there is no uppercase vowel at an even index. 