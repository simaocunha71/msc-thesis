```
function startsOneEnds(n) {
  let count = 0;
  for (let i = 1; i <= 9; i++) {
    count += 1;
  }
  for (let i = 1; i < 10 ** (n - 1); i++) {
    count += 1;
  }
  return count;
}
```


Explanation:
This function counts the numbers of n-digit positive integers that start or end with 1.

The outer loop counts the numbers that start with 1. Since there are 9 possible digits for the remaining n-1 digits, there are 9 such numbers for each of the 10 possible digits that can start the number. Therefore, the number of such numbers is 9 * 10 = 90.

The inner loop counts the numbers that end with 1. Since there are 10 possible digits for the remaining n-1 digits, there are 10 such numbers for each of the 10 possible digits that can end the number. Therefore, the number of such numbers is 10 * 10 = 100.

The total count is the sum of these two counts, which is 90 + 100 = 190.

Note that the function does not consider the case where the number starts and ends with 1, since this is already counted in the outer loop. Therefore, the function returns 190.