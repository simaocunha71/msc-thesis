  return [...new Set(l.sort((a, b) => a - b))];
}

//Test cases
console.log(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])); //[0, 2, 3, 5, 9, 123]

```

## Answer

```javascript
