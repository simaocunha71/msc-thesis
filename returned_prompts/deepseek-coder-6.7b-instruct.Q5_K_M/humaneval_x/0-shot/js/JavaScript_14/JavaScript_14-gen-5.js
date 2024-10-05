  let prefixes = [];
  
  for(let i = 0; i < string.length; i++) {
    prefixes.push(string.slice(0, i + 1));
  }

  return prefixes;
};

console.log(allPrefixes('abc'));

/*
  We can also solve this problem using the `Array.from()` method combined with `Array.prototype.map()`.
  This solution is more elegant and readable.
*/

const allPrefixes2 = (string) => Array.from({ length: string.length }, (_, i) => string.slice(0, i + 1));

console.log(allPrefixes2('abc'));

/*
  If you want to solve this problem using `reduce()` method.
*/

const allPrefixes3 = (string) => string.split('').reduce((acc, _, index) => {
  acc.push(string.slice(0, index + 1));
  return acc;
}, []);

console.log(allPrefixes3('abc'));

```

## JavaScript String – Last Index Of

```javascript
