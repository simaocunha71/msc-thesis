Here is a JavaScript solution for the problem:

```javascript
const fruitDistribution = (s, n) => {
    const [apples, oranges] = s.match(/(\d+) apples and (\d+) oranges/).slice(1).map(Number);
    return n - apples - oranges;
};
```

This solution uses a regular expression to extract the numbers of apples and oranges from the input string. The `match` method returns an array containing the full match and the capture groups (in this case, the numbers of apples and oranges). The `slice(1)` method is used to remove the full match from the array, and the `map(Number)` method is used to convert the strings to numbers.

The function then subtracts the numbers of apples and oranges from the total number of fruits in the basket, and returns the result.