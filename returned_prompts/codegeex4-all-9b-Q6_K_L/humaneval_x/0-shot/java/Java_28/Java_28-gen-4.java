```java
public String concatenate(List<String> strings) {
    StringBuilder result = new StringBuilder();
    for (String s : strings) {
        result.append(s);
    }
    return result.toString();
}
```