```java
public String stringXor(String a, String b) {
    StringBuilder result = new StringBuilder();
    for (int i = 0; i < a.length(); i++) {
        result.append(a.charAt(i) == b.charAt(i) ? '0' : '1');
    }
    return result.toString();
}
```