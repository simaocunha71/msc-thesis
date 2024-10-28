```java
public String stringXor(String a, String b) {
    int len = Math.max(a.length(), b.length());
    StringBuilder result = new StringBuilder(len);
    for (int i = 0; i < len; i++) {
        char charA = i < a.length() ? a.charAt(i) : '0';
        char charB = i < b.length() ? b.charAt(i) : '0';
        result.append((charA ^ charB) == '1' ? '1' : '0');
    }
    return result.toString();
}
```