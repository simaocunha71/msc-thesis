```javascript
const oddCount = (lst) => {
  return lst.map(str => {
    let oddDigits = str.split('').filter(digit => digit % 2 !== 0).length;
    return `the number of odd elements ${oddDigits}n the str${oddDigits}ng ${oddDigits} of the ${oddDigits}nput.`;
  });
}
```