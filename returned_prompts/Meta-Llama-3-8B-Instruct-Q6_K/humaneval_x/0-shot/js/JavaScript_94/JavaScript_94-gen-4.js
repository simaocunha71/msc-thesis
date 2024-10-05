Here is a solution that uses a helper function to check if a number is prime and then finds the largest prime value in the list and returns the sum of its digits:
```
const skjkasdkd = (lst) => {
  const isPrime = (n) => {
    if (n <= 1) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  };

  let largestPrime = -1;
  for (const num of lst) {
    if (isPrime(num) && num > largestPrime) largestPrime = num;
  }

  return largestPrime.toString().split("").reduce((a, b) => a + parseInt(b), 0);
};
```
This solution uses a helper function `isPrime` to check if a number is prime. It then iterates through the list and finds the largest prime value. Finally, it converts the largest prime value to a string, splits it into individual digits, and returns the sum of those digits using the `reduce` method.

Note that this solution assumes that the input list only contains integers. If the list can contain other types of values, you may need to modify the solution accordingly. Also, this solution has a time complexity of O(n), where n is the length of the input list, because it needs to iterate through the list to find the largest prime value. If the list is very large, this solution may be slow. In that case, you may want to consider using a more efficient algorithm or data structure to find the largest prime value.