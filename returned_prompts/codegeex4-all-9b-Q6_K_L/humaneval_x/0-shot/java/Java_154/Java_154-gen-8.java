```java
public boolean cycpatternCheck(String a, String b) {
    for (int i = 0; i < b.length(); i++) {
        if (a.contains(b)) {
            return true;
        }
        b = b.substring(1) + b.charAt(0);
    }
    return false;
}
```