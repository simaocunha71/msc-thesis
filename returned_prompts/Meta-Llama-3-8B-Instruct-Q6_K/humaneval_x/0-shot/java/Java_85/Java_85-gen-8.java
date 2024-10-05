The problem is asking to add the even elements that are at odd indices in a given list of integers. 

Here is the solution in Java:

```java
public int add(List<Integer> lst) {
    int sum = 0;
    for (int i = 1; i < lst.size(); i++) {
        if (lst.get(i) % 2 == 0) {
            sum += lst.get(i);
        }
    }
    return sum;
}
```

In this solution, we iterate over the list using a for loop. We start the loop from the second element (at index 1) because we want to consider only the elements at odd indices. For each element, we check if it is even (i.e., `lst.get(i) % 2 == 0`). If it is even, we add it to the sum. Finally, we return the sum. 

For example, if the input list is `[4, 2, 6, 7]`, the function will return `2` because the even elements at odd indices are `2` and `6`, and their sum is `2`. 