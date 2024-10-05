  return (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z) && (x === y + z || y === x + z || z === x + y));
}

console.log(anyInt(5, 2, 7)); // true
console.log(anyInt(3, 2, 2)); // false
console.log(anyInt(3, -2, 1)); // true
console.log(anyInt(3.6, -2.2, 2)); // false
console.log(anyInt(2, 3, 5)); // true
console.log(anyInt(2, 3, 7)); // false
console.log(anyInt(2, -3, 1)); // true
console.log(anyInt(2.6, -3.2, 2)); // false
```

## 答案

```javascript
const anyInt = (x, y, z) => {
  return (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z) && (x === y + z || y === x + z || z === x + y));
}

console.log(anyInt(5, 2, 7)); // true
console.log(anyInt(3, 2, 2)); // false
console.log(anyInt(3, -2, 1)); // true
console.log(anyInt(3.6, -2.2, 2)); // false
console.log(anyInt(2, 3, 5)); // true
console.log(anyInt(2, 3, 7)); // false
console.log(anyInt(2, -3, 1)); // true
console.log(anyInt(2.6, -3.2, 2)); // false
```

## 解释

这个函数接受三个参数，x，y，z。它首先检查这些参数是否都是整数。如果是，它会检查是否有一个参数等于其他两个参数的和。如果满足这些条件，函数返回true。否则，返回false。

## 测试

```javascript
console.log(anyInt(