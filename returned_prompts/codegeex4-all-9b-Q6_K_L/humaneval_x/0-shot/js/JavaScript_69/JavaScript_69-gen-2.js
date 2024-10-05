To solve this problem, we can follow these steps:

1. Create a dictionary to store the frequency of each integer.
2. Iterate through the list and update the frequency of each integer in the dictionary.
3. Iterate through the dictionary and find the greatest integer that has a frequency greater than or equal to the value of the integer itself.
4. If no such integer exists, return -1.

Here is the implementation in JavaScript:

```javascript
const search = (lst) => {
  const frequency = {};

  // Step 1: Create a dictionary to store the frequency of each integer
  lst.forEach(num => {
    if (frequency[num]) {
      frequency[num]++;
    } else {
      frequency[num] = 1;
    }
  });

  let result = -1;

  // Step 2: Iterate through the dictionary and find the greatest integer
  for (let num in frequency) {
    if (frequency[num] >= num) {
      result = Math.max(result, num);
    }
  }

  return result;
}
```

This solution has a time complexity of O(n), where n is the length of the list.