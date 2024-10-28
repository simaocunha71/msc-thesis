  let str = Array.from(s).map((char, i) => {
    if (char.toLowerCase() !== char.toUpperCase()) {
      return char === char.toLowerCase() ? char.toUpperCase() : char.toLowerCase();
    } else {
      return s.split("").reverse().join("");
    }
  });
  return str.join("");
};

console.log(solve("1234")); // 4321
console.log(solve("ab")); // AB
console.log(solve("#a@C")); // #A@c
```

# 2.

```javascript
