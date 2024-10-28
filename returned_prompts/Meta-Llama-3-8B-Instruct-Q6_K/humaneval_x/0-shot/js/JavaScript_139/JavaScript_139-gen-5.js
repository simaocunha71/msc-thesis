```javascript
const specialFactorial = (n) => {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= i; j++) {
      result *= j;
    }
  }
  return result;
};
```


Explanation:
The function specialFactorial calculates the Brazilian factorial of a given integer n. It uses two nested loops to iterate over the numbers from 1 to n and from 1 to i, respectively. In each iteration, it multiplies the current result by the current number j. The result is initialized to 1 before the loops start. After the loops finish, the function returns the calculated Brazilian factorial. For example, for the input 4, the function will return 288, which is the Brazilian factorial of 4.