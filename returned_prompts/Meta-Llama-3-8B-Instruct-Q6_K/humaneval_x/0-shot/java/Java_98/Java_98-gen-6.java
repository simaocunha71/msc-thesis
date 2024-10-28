Here is a simple solution in Java:

```java
public int countUpper(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i % 2 == 0 && Character.isUpperCase(s.charAt(i))) {
            count++;
        }
    }
    return count;
}
```

This solution iterates over the string `s` and checks each character at an even index to see if it is uppercase using the `Character.isUpperCase` method. If it is, it increments the count. Finally, it returns the count. 

For example, if you call `countUpper("aBCdEf")`, it will return `1` because there is one uppercase vowel at an even index (`'C'` is at index `1`). If you call `countUpper("abcdefg")`, it will return `0` because there are no uppercase vowels at even indices. If you call `countUpper("dBBE")`, it will also return `0` because there are no uppercase vowels at even indices. 

This solution has a time complexity of O(n), where n is the length of the string `s`, because it iterates over the string once. It has a space complexity of O(1), because it uses a constant amount of space to store the count. 

Note that this solution assumes that the input string `s` is not null. If `s` can be null, you should add a check at the beginning of the method to return 0 or throw an exception if `s` is null. 

Here's the modified method:

```java
public int countUpper(String s) {
    if (s == null) {
        return 0;
    }
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i % 2 == 0 && Character.isUpperCase(s.charAt(i))) {
            count++;
        }
    }
    return count;
}
```