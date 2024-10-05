```js
const selectWords = (s, n) => {
  return s.split(' ')
    .filter(word => word.match(/[^aeiouAEIOU ]/g)?.length === n)
}
```
