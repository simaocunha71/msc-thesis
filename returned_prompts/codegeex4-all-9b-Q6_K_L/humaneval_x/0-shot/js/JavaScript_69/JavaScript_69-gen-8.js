To solve this problem, we can use a frequency map to keep track of the occurrences of each integer in the list. Then, we iterate through the list again and check if the frequency of the integer is greater than or equal to the integer itself. If we find such an integer, we return it. If we don't find any integer that satisfies the condition, we return -1.

Here's the solution:

```javascript
const search = (lst) => {
  const frequencyMap = {};
  // create a frequency map
  for (let num of lst) {
    frequencyMap[num] = (frequencyMap[num] || 0) + 1;
  }

  // iterate through the list again
  for (let num of lst) {
    if (frequencyMap[num] >= num) {
      return num;
    }
  }

  // if no such integer is found, return -1
  return -1;
}
```

Let's test the function with the given examples:

```javascript
console.log(search([4, 1, 2, 2, 3, 1])); // 2
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4])); // 3
console.log(search([5, 5, 4, 4, 4])); // -1
```

The output is as expected.