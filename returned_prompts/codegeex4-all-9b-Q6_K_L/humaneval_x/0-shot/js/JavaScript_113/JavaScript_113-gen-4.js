```javascript
const oddCount = (lst) => {
  let str = lst.join(' ');
  let count = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] % 2 !== 0) {
      count++;
    }
  }
  return 'the number of odd elements ' + count + 'n the str' + count + 'ng ' + count + ' of the ' + count + 'nput.';
}
```
