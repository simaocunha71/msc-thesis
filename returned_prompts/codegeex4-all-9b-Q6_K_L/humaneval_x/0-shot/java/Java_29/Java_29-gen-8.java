```java
public List<String> filterByPrefix(List<String> strings, String prefix) {
    return strings.stream()
                  .filter(s -> s.startsWith(prefix))
                  .collect(Collectors.toList());
}
```