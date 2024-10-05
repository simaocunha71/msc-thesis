```java
public String concatenate(List<String> strings) {
    return strings.stream().collect(Collectors.joining());
}
```