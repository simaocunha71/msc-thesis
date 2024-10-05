```java
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for(int i = 0; i < numbers.size(); i++) {
        for(int j = i + 1; j < numbers.size(); j++) {
            if(Math.abs(numbers.get(i) - numbers.get(j)) < threshold) {
                return true;
            }
        }
    }
    return false;
}
```

Explanation:
This solution uses a nested loop to iterate through each pair of numbers in the list. If the absolute difference between any two numbers is less than the threshold, it returns `true`. If no such pair is found, it returns `false`.