```java
public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
    List<Integer> interspersed = new ArrayList<>();
    for (int i = 0; i < numbers.size(); i++) {
        interspersed.add(numbers.get(i));
        if (i < numbers.size() - 1) {
            interspersed.add(delimiter);
        }
    }
    return interspersed;
}
```