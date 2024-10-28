```java
public boolean monotonic(List<Integer> l) {
    int prev = l.get(0);
    for (int i = 1; i < l.size(); i++) {
        int curr = l.get(i);
        if ((prev <= curr && curr <= prev) || (prev >= curr && curr >= prev)) {
            prev = curr;
        } else {
            return false;
        }
    }
    return true;
}
```
In this solution, we initialize a variable `prev` with the first element of the list. Then, we iterate through the list starting from the second element. For each element, we check if it is either less than or equal to the previous element (`prev <= curr`) and the previous element is less than or equal to the current element (`curr <= prev`), or if it is greater than or equal to the previous element (`prev >= curr`) and the previous element is greater than or equal to the current element (`curr >= prev`). If either of these conditions is met, we update the `prev` variable with the current element. If the condition is not met, we return `false` as the list is not monotonically increasing or decreasing. If the loop completes without returning `false`, we return `true` as the list is monotonically increasing or decreasing.