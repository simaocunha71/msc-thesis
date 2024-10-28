Here is the Java solution for the problem:

```java
public boolean cycpatternCheck(String a, String b) {
    int len_a = a.length();
    int len_b = b.length();
    if (len_a < len_b)
        return false;
    String b1 = b + b;
    for (int i = 0; i <= len_a - len_b; i++) {
        String sub = a.substring(i, i + len_b);
        if (sub.equals(b) || sub.equals(b1.substring(i + 1, i + len_b + 1)))
            return true;
    }
    return false;
}
```

This solution works by concatenating the string b with itself, and then checking each substring of length len_b of string a to see if it matches b or any of its rotations. If a match is found, the function returns true. If no match is found after checking all substrings, the function returns false.