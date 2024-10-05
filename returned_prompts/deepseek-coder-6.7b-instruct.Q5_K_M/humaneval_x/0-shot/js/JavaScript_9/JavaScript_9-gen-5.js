  let result = [];
  let currentMax = numbers[0];

  for (let i = 0; i < numbers.length; i++) {
    result.push(currentMax);
    if (numbers[i] > currentMax) {
      currentMax = numbers[i];
    }
  }

  return result;
};

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); //[1, 2, 3, 3, 3, 4, 4]
```

## 2. Find the Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example:

Input: "abcabcbb"
Output: 3 ("abc")

Input: "bbbbbb"
Output: 1 ("b")

Input: "pwwkew"
Output: 3 ("wke")

```javascript
