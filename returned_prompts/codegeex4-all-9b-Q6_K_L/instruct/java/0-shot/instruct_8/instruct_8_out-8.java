```java
public boolean openURL(String url) {
    try {
        Runtime.getRuntime().exec("open " + url);
        return true;
    } catch (IOException e) {
        e.printStackTrace();
        return false;
    }
}
```