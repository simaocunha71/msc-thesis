You can solve this problem by iterating over the list and checking if the index and the element are even. If both conditions are met, add the element to a running sum. Here's how you can implement it in Java:

```java
public int add(List<Integer> lst) {
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (i % 2 == 1 && lst.get(i) % 2 == 0) {
            sum += lst.get(i);
        }
    }
    return sum;
}
```

In this code, `i % 2 == 1` checks if the index is odd, and `lst.get(i) % 2 == 0` checks if the element at the index is even. If both conditions are true, the element is added to the sum.

For example, if you call `add(Arrays.asList(4, 2, 6, 7))`, it will return 2 because the element at index 1 (which is 2) is even.