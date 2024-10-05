Here is the solution in JavaScript:

```javascript
const search = (lst) => {
  const freq = {};
  lst.forEach((num) => {
    if (freq[num]) {
      freq[num]++;
    } else {
      freq[num] = 1;
    }
  });
  for (let num in freq) {
    if (freq[num] >= parseInt(num)) {
      return parseInt(num);
    }
  }
  return -1;
};
```

This function first creates a frequency object where the keys are the numbers in the list and the values are the frequencies. It then iterates over the frequency object and returns the first number that has a frequency greater than or equal to its value. If no such number is found, it returns -1. The function uses parseInt to ensure that the number is converted to an integer before comparing it with its frequency. This is necessary because the frequency object uses strings as keys.