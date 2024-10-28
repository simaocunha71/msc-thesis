The problem is asking to add the even numbers at odd indices in a given list of integers.

Here's a simple solution in Java:

```java
public int add(List<Integer> lst) {
    int sum = 0;
    for (int i = 1; i < lst.size(); i += 2) {
        if (lst.get(i) % 2 == 0) {
            sum += lst.get(i);
        }
    }
    return sum;
}
```

This solution iterates through the list, starting from the second element (index 1), and checks if the element is even by using the modulus operator (`%`). If the element is even, it adds it to the sum. Finally, it returns the sum of the even elements at odd indices.