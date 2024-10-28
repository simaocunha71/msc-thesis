To generate a list of rolling maximum elements, we can iterate through the given list of integers and keep track of the maximum element seen so far. We will start by initializing an empty array to store the rolling maximums and a variable to keep track of the current maximum. As we iterate through the list, we will compare each element with the current maximum and update the current maximum if necessary. We will then push the current maximum to the list of rolling maximums and continue to the next element.

Here's the implementation of the `rollingMax` function in JavaScript:

```javascript
const rollingMax = (numbers) => {
  let max = -Infinity;
  let rollingMaxes = [];

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    rollingMaxes.push(max);
  }

  return rollingMaxes;
}
```

Let's test the function with the example provided:

```javascript
console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]
```

The output is `[1, 2, 3, 3, 3, 4, 4]`, which matches the expected result.