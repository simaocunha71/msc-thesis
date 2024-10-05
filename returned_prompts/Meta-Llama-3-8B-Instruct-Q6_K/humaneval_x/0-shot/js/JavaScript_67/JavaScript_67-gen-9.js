```
const fruitDistribution = (s, n) => {
  const [appleCount, orangeCount] = s.match(/(\d+)\s*apple.*?(\d+)\s*orange/).slice(1).map(Number);
  return n - appleCount - orangeCount;
};
```

Explanation:
The function takes a string `s` that represents the number of apples and oranges and an integer `n` that represents the total number of fruits in the basket.

We use a regular expression to extract the number of apples and oranges from the string. The regular expression `/\d+\s*apple.*?\d+\s*orange/` matches a number followed by " apples" and then " oranges". The `*` operator matches zero or more occurrences of the preceding element, and the `?` operator makes the preceding element optional. The `slice(1)` method is used to remove the first element of the match array, which is the entire match string, and the `map(Number)` method is used to convert the extracted numbers to integers.

Finally, we return the difference between the total number of fruits `n` and the sum of apples and oranges `appleCount + orangeCount`. This gives us the number of mango fruits in the basket.