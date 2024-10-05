```
const fruitDistribution = (s, n) => {
  const fruit = s.match(/\d+/g).map(Number);
  const apples = fruit[0];
  const oranges = fruit[1];
  return n - apples - oranges;
};
```
This function uses a regular expression to extract the numbers of apples and oranges from the input string. The `match()` method returns an array of strings that match the regular expression, and the `map()` method converts these strings to numbers. The function then subtracts the number of apples and oranges from the total number of fruits in the basket to find the number of mangoes.