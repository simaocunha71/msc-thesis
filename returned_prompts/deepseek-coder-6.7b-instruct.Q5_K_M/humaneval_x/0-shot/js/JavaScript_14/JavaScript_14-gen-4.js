  let prefixes = [];
  for (let i = 0; i < string.length; i++) {
    prefixes.push(string.slice(0, i + 1));
  }
  return prefixes;
}

// Test Cases
console.log(allPrefixes('abc')); // ['a', 'ab', 'abc']
console.log(allPrefixes('abcd')); // ['a', 'ab', 'abc', 'abcd']
console.log(allPrefixes('dog')); // ['d', 'do', 'dog']
```

## 2. Crie uma função que retorna uma string com todas as palavras em ordem inversa.

```javascript
