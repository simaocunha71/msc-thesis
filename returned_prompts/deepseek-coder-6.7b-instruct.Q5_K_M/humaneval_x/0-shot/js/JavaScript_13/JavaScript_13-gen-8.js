  let temp;
  while(b !== 0){
    temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

module.exports = greatestCommonDivisor;
```

## 2.2 欧几里得距离

欧几里得距离是欧几里得空间中两点之间“欧氏距离”的度量。在n维空间中，点Pi=(xi)和Pj=(xj)之间的欧氏距离定义为√((xi-xj)^2 + ... + (xn-xn)^2)。

```javascript
// 欧几里得距离
