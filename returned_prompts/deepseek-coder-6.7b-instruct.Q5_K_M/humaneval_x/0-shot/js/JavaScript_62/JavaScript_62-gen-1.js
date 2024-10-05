  return xs.slice(1).map((v, i) => (i + 1) * v);
};

console.log(derivative([3, 1, 2, 4, 5]));
console.log(derivative([1, 2, 3]));
```

---

# Solution

```javascript
