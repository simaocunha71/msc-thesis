You can use a variable to keep track of the current balance and iterate over the operations. If the balance ever falls below zero, return true. If you finish iterating over all operations without the balance ever falling below zero, return false.

Here is a Java solution:

```java
public boolean belowZero(List<Integer> operations) {
    int balance = 0;
    for (int operation : operations) {
        balance += operation;
        if (balance < 0) {
            return true;
        }
    }
    return false;
}
```

This solution has a time complexity of O(n), where n is the number of operations, because it needs to iterate over all operations once. The space complexity is O(1), because it only uses a constant amount of space. 