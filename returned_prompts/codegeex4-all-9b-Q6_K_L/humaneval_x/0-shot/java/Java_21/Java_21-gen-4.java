```java
public List<Double> rescaleToUnit(List<Double> numbers) {
    // TODO: implement this method
    double min = Double.MAX_VALUE;
    double max = Double.MIN_VALUE;
    for (double d : numbers) {
        if (d < min) min = d;
        if (d > max) max = d;
    }
    List<Double> result = new ArrayList<>();
    for (double d : numbers) {
        result.add((d - min) / (max - min));
    }
    return result;
}
```
