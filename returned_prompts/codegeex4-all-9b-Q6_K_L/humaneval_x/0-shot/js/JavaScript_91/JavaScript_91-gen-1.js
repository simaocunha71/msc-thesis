Here is the JavaScript solution for the problem:

```javascript
const isBored = (S) => {
  const regex = /I\.|I\?|I!/g;
  const matches = S.match(regex);
  return matches ? matches.length : 0;
};
```

Explanation:
We are using a regular expression to match the sentences that start with "I". The regular expression `/I\.|I\?|I!/g` matches "I." "I?" or "I!".
We are using the `match` function to get all the matches in the string. If there are no matches, `match` returns `null`. In this case, we return `0` as there are no boredoms.
If there are matches, we return the length of the matches array, which gives the number of boredoms.