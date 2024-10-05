The problem can be solved by extracting the numbers from the string and subtracting them from the total number of fruits. Here is a solution in JavaScript:

```javascript
const fruitDistribution = (s, n) => {
  let countApples = parseInt(s.split('apples')[0]);
  let countOranges = parseInt(s.split('oranges')[0].split('and')[1]);
  return n - countApples - countOranges;
}
```

In this solution, we first split the string by 'apples' and take the first part. Then we split this part by 'and' and take the first number (which is the number of apples). Similarly, we split the string by 'oranges' and take the first part, split it by 'and' and take the second number (which is the number of oranges). Finally, we subtract the number of apples and oranges from the total number of fruits to get the number of mangoes.