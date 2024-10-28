```java
public String sortNumbers(String numbers) {
    String[] parts = numbers.split(" ");
    Arrays.sort(parts);
    return String.join(" ", parts);
}
```
Explanation:
The task is to sort the given string of numbers from 'zero' to 'nine' in ascending order. 

To achieve this, we split the input string into an array of strings using the `split()` method with a space character as the delimiter. This gives us an array of strings, each representing a number.

Next, we use the `Arrays.sort()` method to sort this array in ascending order.

Finally, we use the `String.join()` method to concatenate the sorted array of strings into a single string, with a space character as the delimiter. This gives us the final sorted string.

For example, if the input is "three one five", the output will be "one three five".