You can solve this problem by using a loop to iterate from 1 to n. If the current index is even, you calculate the factorial of the index using a recursive function. Otherwise, you calculate the sum of numbers from 1 to the index. Here is the implementation in JavaScript:

```javascript
const f = (n) => {
  const factorial = (num) => {
    if (num === 0 || num === 1) return 1;
    return num * factorial(num - 1);
  };

  const sum = (num) => {
    let total = 0;
    for (let i = 1; i <= num; i++) {
      total += i;
    }
    return total;
  };

  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(factorial(i));
    } else {
      result.push(sum(i));
    }
  }
  return result;
};

console.log(f(5)); // [1, 2, 6, 24, 15]
```

The `factorial` function calculates the factorial of a number by recursively multiplying the number with the factorial of the previous number. The `sum` function calculates the sum of numbers from 1 to a given number using a loop. The main function `f` uses these helper functions to calculate the required values and returns the final list.