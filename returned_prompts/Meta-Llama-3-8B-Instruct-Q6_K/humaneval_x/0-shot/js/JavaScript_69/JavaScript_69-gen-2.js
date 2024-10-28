```
const search = (lst) => {
  const frequencyMap = {};
  for (const num of lst) {
    frequencyMap[num] = (frequencyMap[num] || 0) + 1;
  }
  let maxFreq = 0;
  let maxNum = -1;
  for (const [num, freq] of Object.entries(frequencyMap)) {
    if (freq >= num && freq > maxFreq) {
      maxFreq = freq;
      maxNum = num;
    }
  }
  return maxNum > 0 ? maxNum : -1;
};
```


Explanation:

1. We create an object `frequencyMap` to store the frequency of each number in the list.
2. We iterate over the list and for each number, we increment its frequency in the `frequencyMap`.
3. We initialize `maxFreq` and `maxNum` to keep track of the maximum frequency and the corresponding number.
4. We iterate over the `frequencyMap` and for each number, we check if its frequency is greater than or equal to the number itself and greater than `maxFreq`. If it is, we update `maxFreq` and `maxNum`.
5. Finally, we return `maxNum` if it is greater than 0, otherwise we return -1.