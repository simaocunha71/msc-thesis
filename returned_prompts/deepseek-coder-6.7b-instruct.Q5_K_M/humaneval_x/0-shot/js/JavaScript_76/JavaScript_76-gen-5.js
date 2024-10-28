  if(n<=0 || x<=0) return false;
  let res = Math.log(x)/Math.log(n);
  return Number.isInteger(res);
};
console.log(isSimplePower(1, 4));
console.log(isSimplePower(2, 2));
console.log(isSimplePower(8, 2));
console.log(isSimplePower(3, 2));
console.log(isSimplePower(3, 1));
console.log(isSimplePower(5, 3));
```

## 3. 回文数

回文数是指一个整数或字符串在反向读取时仍然保持相同。

```javascript
