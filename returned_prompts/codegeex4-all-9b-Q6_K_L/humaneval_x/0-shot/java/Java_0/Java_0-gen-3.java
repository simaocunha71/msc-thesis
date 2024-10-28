```java
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size() - 1; i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double diff = Math.abs(numbers.get(i) - numbers.get(j));
            if (diff < threshold) {
                return true;
            }
        }
    }
    return false;
}
```