To solve this problem, we can use the `reduce` function in JavaScript along with the `map` function. Here's an example of how you could implement this function:

```javascript
const stringXor = (a, b) => {
  // Convert the strings to arrays of numbers
  const aArr = a.split('').map(Number);
  const bArr = b.split('').map(Number);

  // Use reduce to perform XOR on each corresponding pair of numbers
  const resultArr = aArr.reduce((acc, curr, index) => {
    const xor = curr ^ bArr[index];
    acc.push(xor);
    return acc;
  }, []);

  // Convert the result array back to a string
  const result = resultArr.join('');
  return result;
}
```

In this solution, we first convert the input strings `a` and `b` into arrays of numbers using the `split` and `map` functions. Then we use the `reduce` function to perform XOR on each corresponding pair of numbers in the arrays. Finally, we convert the resulting array back to a string using the `join` function and return it.