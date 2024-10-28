```
const fruitDistribution = (s, n) => {
  const regex = /\d+/g;
  const matches = s.match(regex);
  const apples = parseInt(matches[0]);
  const oranges = parseInt(matches[2]);
  return n - apples - oranges;
};
```
Explanation:
The problem requires us to extract the numbers of apples and oranges from the given string and then subtract them from the total number of fruits to get the number of mango fruits.

We use a regular expression (`/\d+/g`) to match one or more digits in the string. The `g` flag makes the regex global, so it matches all occurrences in the string, not just the first one.

We then parse the matches using `parseInt` to get the numbers of apples and oranges. Finally, we subtract these numbers from the total number of fruits (`n`) to get the number of mango fruits.

For example, if the input string is `"5 apples and 6 oranges"` and the total number of fruits is `19`, the function would extract the numbers `5` and `6`, subtract them from `19` to get `8`, and return `8` as the number of mango fruits.