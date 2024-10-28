```javascript
function uniqueTokens(str1, str2) {
  let result = '';
  let tokens1 = str1.split(' ');
  let tokens2 = str2.split(' ');

  for (let i = 0; i < tokens1.length; i++) {
    let token = tokens1[i];
    for (let j = 0; j < tokens2.length; j++) {
      if (token === tokens2[j]) {
        continue;
      }
    }
    result += token + ' ';
  }

  return result.trim();
}
```