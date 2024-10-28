```java
public List<Double> rescaleToUnit(List<Double> numbers) {
        double max = Double.MIN_VALUE;
        double min = Double.MAX_VALUE;
        for (Double number : numbers) {
            max = Math.max(number, max);
            min = Math.min(number, min);
        }
        List<Double> result = new ArrayList<>();
        for (Double number : numbers) {
            result.add((number - min) / (max - min));
        }
        return result;
    }
```