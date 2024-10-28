  return string.split('').map((char) => {
    return char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
  }).join('');
}

console.log(flipCase('Hello'));
// Expected output: 'hELLO'

```

## 2. Calculate the factorial of a number

```javascript
