```javascript
const removeVowels = (text) => {
  if (text.length === 0) return '';
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  let newText = '';
  for (let i = 0; i < text.length; i++) {
    if (!vowels.includes(text[i].toLowerCase())) {
      newText += text[i];
    }
  }
  return newText;
}
```
