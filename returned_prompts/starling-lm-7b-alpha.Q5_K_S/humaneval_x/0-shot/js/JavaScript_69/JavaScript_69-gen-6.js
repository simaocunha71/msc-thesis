/*
Here's a function that takes a list of positive integers and returns the greatest integer that is greater than 0, and has a frequency greater than or equal to the value of the integer itself. If no such a value exist, it returns -1.

The function starts by initializing an empty object called "counts" to keep track of the frequency of each integer in the list. It then iterates through the list using the `forEach` method. For each integer, it checks if the integer already exists as a key in the "counts" object. If it does, it increments the corresponding value by 1. If it doesn't, it adds the integer as a new key in the "counts" object and sets its value to 1.

After counting the frequency of each integer, the function creates an empty array called "candidates" to store the integers that have a frequency greater than or equal to their own value. It then iterates through the "counts" object using a `for...in` loop. For each key (integer), it checks if the value (frequency) is greater than or equal to the key itself. If it is, the key (integer) is added to the "candidates" array.

Finally, the function checks if the "candidates" array is empty. If it is, it means that no such integer exists, so the function returns -1. Otherwise, it returns the greatest integer in the "candidates" array using the `Math.max` function.

This implementation has a time complexity of O(n) because it only needs to iterate through the input list and the "counts" object once. The space complexity is also O(n) because the "counts" object can have at most n keys, where n is the length of the input list.
*/

  const counts = {};
  lst.forEach(num => {
    counts[num] = (counts[num] || 0) + 1;
  });

  const candidates = Object.keys(counts).filter(num => counts[num] >= parseInt(num));

  return candidates.length ? Math.max(...candidates) : -1;
};

search([4, 1, 2, 2, 3, 1]); // returns 2