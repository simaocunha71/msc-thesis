```java
public double meanAbsoluteDeviation(List<Double> numbers) {
        double avg = numbers.stream().mapToDouble(Double::doubleValue).average().orElse(0);
        return numbers.stream().mapToDouble(d -> Math.abs(d - avg)).average().orElse(0);
    }
```