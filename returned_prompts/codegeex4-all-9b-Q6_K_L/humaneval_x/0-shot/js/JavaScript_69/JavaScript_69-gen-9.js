```js
const search = (lst) => {
  let num_freq = {};
  for (let i = 0; i < lst.length; i++) {
    if (num_freq[lst[i]]) {
      num_freq[lst[i]]++;
    } else {
      num_freq[lst[i]] = 1;
    }
  }
  let max_freq = 0;
  for (let num in num_freq) {
    max_freq = Math.max(max_freq, num_freq[num]);
  }
  for (let num in num_freq) {
    if (num_freq[num] >= num) {
      return num;
    }
  }
  return -1;
}
```

Let's break down the solution:

1. We create a dictionary to store the frequencies of each number in the list.
2. We iterate through the list and update the frequency of each number in the dictionary.
3. We find the maximum frequency of any number in the list.
4. We iterate through the dictionary and return the number if its frequency is greater than or equal to its value.
5. If no such number exists, we return -1.

This solution has a time complexity of O(n) where n is the length of the list.