Here is a JavaScript function that fulfills the task:

```javascript
const fruitDistribution = (s, n) => {
    let [apples, oranges] = s.match(/(\d+)\s*apple(s)?\s*and\s*(\d+)\s*orange(s)?/).slice(1).map(Number);
    return n - apples - oranges;
}
```

The function `fruitDistribution` takes two parameters, a string `s` and an integer `n`. It uses regular expression to extract the number of apples and oranges from the string. The regular expression `/(\d+)\s*apple(s)?\s*and\s*(\d+)\s*orange(s)?/` matches a pattern that includes one or more digits (`\d+`) followed by either "apple" or "apples" (with optional "s" at the end), followed by "and", followed by one or more digits, followed by either "orange" or "oranges" (with optional "s" at the end). The `match` method returns an array of matches, and we use `slice(1)` to remove the first element of the array (which is the entire matched string), and `map(Number)` to convert the matched numbers to integers. Finally, we return the difference between `n` and the sum of the numbers of apples and oranges.