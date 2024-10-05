```js
const oddCount = (lst) => {
  return lst.map(str => {
    const oddDigits = str.split('').filter(digit => digit % 2 !== 0).length;
    return `the number of odd elements ${oddDigits}n the str${oddDigits}ng ${oddDigits} of the ${oddDigits}nput.`;
  });
}
```
