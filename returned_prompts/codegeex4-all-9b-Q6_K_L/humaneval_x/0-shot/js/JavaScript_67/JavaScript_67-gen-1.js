You can use the `split` method to separate the string into individual words and then use the `map` method to convert the number of apples and oranges to integers. Finally, you can subtract the sum of apples and oranges from the total number of fruits to get the number of mangoes. Here's the solution:

```javascript
const fruitDistribution = (s, n) => {
  const words = s.split(' ');
  const apples = parseInt(words[0]);
  const oranges = parseInt(words[4]);
  return n - apples - oranges;
};
```

This solution assumes that the string will always be in the format "x apples and y oranges". If the format can vary, you may need to add additional checks to handle different cases.