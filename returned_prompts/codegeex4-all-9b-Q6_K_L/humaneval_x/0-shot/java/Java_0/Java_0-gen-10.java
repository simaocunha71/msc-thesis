```java
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (Math.abs(numbers.get(i) - numbers.get(j)) < threshold) {
                return true;
            }
        }
    }
    return false;
}
```

Explanation:
The function `hasCloseElements` takes a list of numbers and a threshold as input. It iterates through the list and checks if any two numbers are closer to each other than the given threshold. If it finds such a pair, it returns `true`. If it doesn't find any such pair, it returns `false`.

The time complexity of this solution is O(n^2), where n is the size of the input list. This is because we are using nested loops to compare every pair of numbers in the list.