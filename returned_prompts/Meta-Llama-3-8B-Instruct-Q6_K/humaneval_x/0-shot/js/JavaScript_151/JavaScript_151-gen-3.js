```
function doubleTheDifference(lst) {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (Number.isInteger(lst[i]) && lst[i] >= 0 && lst[i] % 2 !== 0) {
      sum += lst[i] ** 2;
    }
  }
  return sum;
}
```


Explanation:
The function `doubleTheDifference` iterates over the input list `lst`. For each element, it checks if it's an integer, non-negative and odd. If it is, it adds the square of the element to the sum. Finally, it returns the sum.

The `Number.isInteger` method is used to check if the element is an integer. The `lst[i] >= 0` condition is used to ignore negative numbers. The `lst[i] % 2 !== 0` condition is used to check if the number is odd. The `**` operator is used to calculate the square of the number. The `sum` variable is initialized to 0 and updated in each iteration of the loop. If the input list is empty, the function will return 0 as per the problem statement.