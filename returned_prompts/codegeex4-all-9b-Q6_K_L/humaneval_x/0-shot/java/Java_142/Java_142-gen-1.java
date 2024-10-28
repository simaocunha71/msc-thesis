Here is the solution to the problem:

```java
public int sumSquares(List<Integer> lst) {
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (i % 3 == 0) {
            sum += Math.pow(lst.get(i), 2);
        } else if (i % 4 == 0) {
            sum += Math.pow(lst.get(i), 3);
        } else {
            sum += lst.get(i);
        }
    }
    return sum;
}
```
This function iterates over the list and performs the required operations based on the index of the element. If the index is a multiple of 3, it squares the element. If the index is a multiple of 4 and not a multiple of 3, it cubes the element. Otherwise, it just adds the element to the sum. Finally, it returns the sum.