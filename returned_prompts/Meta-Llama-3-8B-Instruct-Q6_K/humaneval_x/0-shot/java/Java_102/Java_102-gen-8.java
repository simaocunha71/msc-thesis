```java
public int chooseNum(int x, int y) {
    if (x > y) {
        int temp = x;
        x = y;
        y = temp;
    }
    for (int i = x; i <= y; i++) {
        if (i % 2 == 0) {
            return i;
        }
    }
    return -1;
}
```
Explanation:
The function first checks if x is greater than y. If so, it swaps them to ensure that x is less than or equal to y. Then it iterates over the range [x, y] (inclusive) and checks if each number is even (i.e., i % 2 == 0). If it finds an even number, it returns that number. If it doesn't find any even numbers in the range, it returns -1. 

For example, if x = 12 and y = 15, the function will return 14, which is the biggest even number in the range [12, 15]. If x = 13 and y = 12, the function will return -1, because there are no even numbers in the range [13, 12]. 

Note: This function assumes that x and y are positive integers. If x or y could be negative or non-integer, additional checks would be needed. 