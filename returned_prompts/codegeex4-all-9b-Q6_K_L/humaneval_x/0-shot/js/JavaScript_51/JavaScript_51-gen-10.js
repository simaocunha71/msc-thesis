```js
const removeVowels = (text) => {
  return text.split('').filter(x => !'aeiouAEIOU'.includes(x)).join('');
}
```