Here is the solution:

```javascript
const eat = (number, need, remaining) => {
  const eaten = number + Math.min(need, remaining);
  const left = remaining - (eaten - number);
  return [eaten, left];
};
```

Explanation:
The function `eat` takes three parameters: `number`, `need`, and `remaining`. It calculates the total number of carrots eaten by adding the initial number of carrots eaten (`number`) to the minimum of the remaining carrots (`remaining`) and the number of carrots needed (`need`). The number of carrots left is calculated by subtracting the difference between the total number of carrots eaten and the initial number of carrots eaten from the remaining carrots. The function returns an array containing the total number of carrots eaten and the number of carrots left.