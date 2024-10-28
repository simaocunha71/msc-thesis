  const evenIdx = l.filter((_, idx) => idx % 2 === 0);
  evenIdx.sort((a, b) => a - b);

  return l.map((_, idx) => (idx % 2 === 0 ? evenIdx.shift() : l[idx]));
}

console.log(sortEven([1, 2, 3])) // [1, 2, 3]
console.log(sortEven([5, 6, 3, 4])) // [3, 6, 5, 4]
```

## 3. 점수 집계
```javascript
