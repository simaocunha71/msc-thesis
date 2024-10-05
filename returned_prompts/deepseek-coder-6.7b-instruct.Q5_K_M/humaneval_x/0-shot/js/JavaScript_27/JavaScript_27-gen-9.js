return string.split('').map(char => {
    return char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
  }).join('');

};

console.log(flipCase('Hello')); // 'hELLO'
```

## 10. Repeat String

```javascript
