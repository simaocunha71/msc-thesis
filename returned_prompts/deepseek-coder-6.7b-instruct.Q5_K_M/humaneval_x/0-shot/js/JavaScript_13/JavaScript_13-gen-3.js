  if (b === 0) {
    return a;
  }
  return greatestCommonDivisor(b, a % b);
};
```

### 3. 斐波那契数列

斐波那契数列是一个数列，其中每个数都是其前两个数之和，通常从0和1开始。

斐波那契数列的生成函数可以写成递归形式。

```javascript
