```java
public int vowelsCount(String s) {
    int vowels = 0;
    String vowelsStr = "aeiou";
    s = s.toLowerCase();
    for (int i = 0; i < s.length(); i++) {
        if (vowelsStr.contains(String.valueOf(s.charAt(i)))) {
            vowels++;
        } else if (i == s.length() - 1 && s.charAt(i) == 'y') {
            vowels++;
        }
    }
    return vowels;
}
```