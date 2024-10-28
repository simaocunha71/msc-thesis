  return ((x == y + z) && (typeof x == 'number') && (typeof y == 'number') && (typeof z == 'number') && Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z));
}

console.log(anyInt(5, 2, 7)); // ➞ true
console.log(anyInt(3, 2, 2)); // ➞ false
console.log(anyInt(3, -2, 1)); // ➞ true
console.log(anyInt(3.6, -2.2, 2)); // ➞ false


```

## JavaScript

```javascript

