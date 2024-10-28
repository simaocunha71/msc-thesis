```
function startsOneEnds(n) {
    let count = 0;
    for (let i = 1; i <= 9; i++) {
        for (let j = 0; j < n - 1; j++) {
            count += 1;
        }
        if (i === 1) {
            count++;
        }
        if (i === 9) {
            count++;
        }
    }
    return count;
}
```
In this solution, we iterate through all possible leading digits (1-9) and for each leading digit, we iterate through all possible digits (0-9) except the last digit which is fixed as the leading digit. We increment the count for each valid number. Finally, we increment the count by 1 for numbers that start or end with 1. The time complexity is O(n) and the space complexity is O(1). 

Note: This solution assumes that the input n is a positive integer. If n can be 0, you should add a condition to handle it. 

Also, this solution can be optimized by using mathematical formulas to calculate the count. For example, the count of numbers that start with 1 is 9^(n-1) and the count of numbers that end with 1 is 10^(n-1) - 9^(n-1). The total count is the sum of these two counts. The optimized solution would be:

```
function startsOneEnds(n) {
    return 9**(n-1) + 10**(n-1) - 9**(n-1);
}
```


This optimized solution has a time complexity of O(1) and a space complexity of O(1). It is more efficient than the original solution, especially for large values of n.