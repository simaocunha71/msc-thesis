Here is the solution for the problem. This method takes a list of double numbers and a threshold as parameters, and returns true if there are any two numbers in the list that are closer to each other than the threshold, and false otherwise.

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

This solution works by iterating over the list of numbers with two nested loops. For each pair of numbers, it calculates the absolute difference between the two numbers and checks if this difference is less than the threshold. If it finds a pair of numbers with a difference less than the threshold, it immediately returns true. If it doesn't find any such pair after checking all numbers, it returns false.

You can test this method with the examples you provided:

```java
System.out.println(hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)); // prints false
System.out.println(hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)); // prints true
``` 