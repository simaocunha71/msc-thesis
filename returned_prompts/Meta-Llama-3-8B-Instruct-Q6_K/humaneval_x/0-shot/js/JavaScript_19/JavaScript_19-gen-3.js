```
const sortNumbers = (numbers) => {
  const numMap = {
    zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9
  };
  const nums = numbers.split(' ');
  const sortedNums = nums.sort((a, b) => numMap[a] - numMap[b]);
  return sortedNums.join(' ');
};
```


Explanation:
This function first defines a mapping of the number words to their numerical values. It then splits the input string into an array of words using the `split` method with a space character as the separator. It then sorts this array using the `sort` method, providing a compare function that uses the `numMap` to compare the numerical values of the words. Finally, it joins the sorted array back into a string using the `join` method with a space character as the separator. The resulting string is the input string with the numbers sorted from smallest to largest.