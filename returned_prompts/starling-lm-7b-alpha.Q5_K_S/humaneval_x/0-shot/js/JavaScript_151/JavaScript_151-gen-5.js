To solve this problem, we first need to filter out the odd numbers from the list. We can achieve this by using the `filter()` method on the list. Then, we need to square each of the odd numbers and sum them up. We can use the `map()` method along with the `reduce()` method to achieve this. Finally, we return the sum of the squared odd numbers.

Here's the code:

```javascript
const doubleTheDifference = (lst) => {
  const oddNums = lst.filter((num) => Number.isInteger(num) && num % 2 !== 0);
  const squaredOddNums = oddNums.map((num) => num * num);
  return squaredOddNums.reduce((acc, curr) => acc + curr, 0);
};
```

In the `filter()` method, we check if the number is an integer and if it is odd. If both conditions are met, we include the number in the `oddNums` array.

In the `map()` method, we square each of the odd numbers in the `oddNums` array and store the result in the `squaredOddNums` array.

Finally, we use the `reduce()` method to sum up all the squared odd numbers in the `squaredOddNums` array. We initialize the accumulator (`acc`) to 0 and for each number in the array, we add it to the accumulator. The result is returned as the final sum of the squared odd numbers.

You can test the code with the provided test cases to verify its correctness.

Hope this helps!

Here are some additional resources for further learning:

- [Array.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
- [Array.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
- [Array.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)

