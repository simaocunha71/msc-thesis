```java
public int vowelsCount(String s) {
    int count = 0;
    for (char c : s.toCharArray()) {
        if ("aeiouAEIOU".indexOf(c) != -1) {
            count++;
        }
    }
    if (s.length() > 0 && "aeiouAEIOU".indexOf(s.charAt(s.length() - 1)) != -1) {
        count++;
    }
    return count;
}
```