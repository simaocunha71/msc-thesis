```javascript
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, curr, index) => {
    if (index === 0) {
      return [curr];
    }
    return acc.concat([delimeter, curr]);
  }, []);
};
```
Explanation:
This solution is similar to the previous one, but it adds the