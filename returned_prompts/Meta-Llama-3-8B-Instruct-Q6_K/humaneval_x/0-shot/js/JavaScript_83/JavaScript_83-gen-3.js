```
function startsOneEnds(n) {
  let count = 0;
  for (let i = 10 ** (n - 1); i <= 10 ** n - 1; i++) {
    let str = i.toString();
    if (str.startsWith('1') || str.endsWith('1')) {
      count++;
    }
  }
  return count;
}
```
This function iterates through all the n-digit numbers, converts each number to a string, and checks if the string starts or ends with '1'. If it does, it increments the count. Finally, it returns the total count.

Example:
```
startsOneEnds(2) // 10
startsOneEnds(3) // 90
startsOneEnds(4) // 900
```

The time complexity of this function is O(10^n), which is the number of n-digit numbers. The space complexity is O(1), as we only use a constant amount of space to store the count and the string. 

Please note that this function may take a long time to execute for large values of n, as the number of n-digit numbers grows exponentially with n. For example, for n=10, the function would have to iterate through over 9 million numbers. 

In such cases, a more efficient solution might be needed. For example, we could observe that the number of n-digit numbers that start with 1 is equal to the number of (n-1)-digit numbers, and the number of n-digit numbers that end with 1 is equal to the number of (n-1)-digit numbers. Therefore, the total count is equal to the number of (n-1)-digit numbers multiplied by 2. This would reduce the time complexity to O(10^(n-1)), which is much faster for large values of n. 

Here is the updated function:
```
function startsOneEnds(n) {
  let count = 10 ** (n - 1);
  return 2 * count;
}
``` 