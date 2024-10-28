```javascript
function solve(N) {
  let sum = 0;
  let binary = N.toString(2);
  for (let i = 0; i < binary.length; i++) {
    sum += parseInt(binary[i], 10);
  }
  return sum.toString();
}
```


Explanation:
The given problem is to find the total sum of the digits of a given positive integer N in binary. 

First, we convert the given integer N to a binary string using the `toString(2)` method. 

Then, we initialize a variable `sum` to store the sum of the digits. 

Next, we loop through each character in the binary string using a `for` loop. 

Inside the loop, we convert each character to an integer using `parseInt(binary[i], 10)` and add it to the `sum`. 

Finally, we return the `sum` as a string using `toString()`.

This solution works for all the given constraints and the provided examples. It correctly calculates the sum of the digits in binary for any given positive integer N.