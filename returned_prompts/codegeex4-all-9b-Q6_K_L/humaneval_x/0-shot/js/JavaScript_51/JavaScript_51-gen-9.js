```js
const removeVowels = (text) => {
  let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  return text.split('').filter((char) => !vowels.includes(char)).join('');
}
```