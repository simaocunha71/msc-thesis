```java
public String concatenate(List<String> strings) {
    if (strings == null || strings.isEmpty()) {
        return "";
    }

    StringBuilder sb = new StringBuilder();
    for (String s : strings) {
        sb.append(s);
    }
    return sb.toString();
}
```