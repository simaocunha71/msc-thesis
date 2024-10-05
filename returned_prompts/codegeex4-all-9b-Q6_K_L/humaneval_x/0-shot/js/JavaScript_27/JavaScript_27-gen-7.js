```javascript
const flipCase = (string) => {
  let result = '';
  for (let i = 0; i < string.length; i++) {
    let char = string[i];
    if (char === char.toUpperCase()) {
      result += char.toLowerCase();
    } else {
      result += char.toUpperCase();
    }
  }
  return result;
}
```

B:
```javascript
const flipCase = (string) => {
  return string.split('').map(char => char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase()).join('');
}
```

C:
```javascript
const flipCase = (string) => {
  return string
    .split('')
    .map(char => char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase())
    .join('');
}
```

D:
```javascript
const flipCase = (string) => {
  let result = '';
  for (let i = 0; i < string.length; i++) {
    let char = string[i];
    if (char === char.toUpperCase()) {
      result += char.toLowerCase();
    } else {
      result += char.toUpperCase();
    }
  }
  return result;
}
```

E:
```javascript
const flipCase = (string) => {
  return string
    .split('')
    .map(char => char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase())
    .join('');
}
```

F:
```javascript
const flipCase = (string) => {
  return string
    .split('')
    .map(char => char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase())
    .join('');
}
```

G:
```javascript
const flipCase = (string) => {
  return string
    .split('')
    .map(char => char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase())
    .join('');
}
```

H:
```javascript
const flipCase = (string) => {
  return string
    .split('')
    .map(char => char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase())
    .join('');
}
```