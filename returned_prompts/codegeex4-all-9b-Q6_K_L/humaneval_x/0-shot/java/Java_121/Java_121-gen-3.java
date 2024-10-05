Here is a Java solution for the problem:

```java
public int solution(List<Integer> lst) {
    int sum = 0;
    for (int i = 0; i < lst.size(); i += 2) {
        if (lst.get(i) % 2 != 0) {
            sum += lst.get(i);
        }
    }
    return sum;
}
```

This solution iterates over the list with a step of 2, which ensures that it only checks elements in even positions. For each element, it checks if it is odd. If it is, it adds it to the sum. Finally, it returns the sum of all odd elements in even positions.