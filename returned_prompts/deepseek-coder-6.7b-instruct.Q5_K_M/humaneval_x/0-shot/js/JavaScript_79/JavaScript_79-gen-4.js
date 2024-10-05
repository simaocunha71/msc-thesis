  return 'db' + decimal.toString(2) + 'db';
}

console.log(decimalToBinary(15)); // returns "db1111db"
console.log(decimalToBinary(32)); // returns "db100000db"
console.log(decimalToBinary(255)); // returns "db1111111db"
console.log(decimalToBinary(1024)); // returns "db1000000000db"
console.log(decimalToBinary(0)); // returns "db0db"
```

## 10. The Function `binaryToDecimal`
```javascript
