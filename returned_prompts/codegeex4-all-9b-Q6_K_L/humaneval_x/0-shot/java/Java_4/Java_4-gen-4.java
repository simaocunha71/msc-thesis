```java
public double meanAbsoluteDeviation(List<Double> numbers) {
    if (numbers == null || numbers.size() == 0) {
        throw new IllegalArgumentException("numbers should not be empty");
    }
    double mean = 0.0;
    for (Double num : numbers) {
        mean += num;
    }
    mean /= numbers.size();
    double mad = 0.0;
    for (Double num : numbers) {
        mad += Math.abs(num - mean);
    }
    return mad / numbers.size();
}
```
