  if (b === 0)
    return a;
  return greatestCommonDivisor(b, a % b);
};

module.exports = greatestCommonDivisor;
```

## Solution 2:

```javascript
