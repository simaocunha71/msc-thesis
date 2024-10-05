  let triples = 0;
  let squares = Array(n+1).fill(0).map((_, i) => i * i - i + 1);

  for (let i = 1; i < n - 1; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k <= n; k++) {
        if ((squares[i] + squares[j] + squares[k]) % 3 === 0) {
          triples++;
        }
      }
    }
  }

  return triples;
}

console.log(getMaxTriples(5));
// Output: 1

// Time Complexity: O(n^3)
// Space Complexity: O(n)
```

# 8. 3Sum Closest
```javascript
