```java
public int doubleTheDifference(List<Object> lst) {
    if (lst.isEmpty()) {
        return 0;
    }
    int sum = 0;
    for (Object o : lst) {
        if (o instanceof Integer) {
            int num = (int) o;
            if (num % 2 != 0) {
                sum += num * num;
            }
        }
    }
    return sum;
}
```

This solution first checks if the input list is empty and returns 0 if it is. Then, it iterates over each element in the list. If the element is an integer and is odd, it squares the integer and adds it to the sum. Finally, it returns the sum.