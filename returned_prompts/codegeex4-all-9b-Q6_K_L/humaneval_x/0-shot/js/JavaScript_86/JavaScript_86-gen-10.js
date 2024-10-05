```javascript
  return s.split(' ')
          .map(w => w.split('').sort().join(''))
          .join(' ');
};
```