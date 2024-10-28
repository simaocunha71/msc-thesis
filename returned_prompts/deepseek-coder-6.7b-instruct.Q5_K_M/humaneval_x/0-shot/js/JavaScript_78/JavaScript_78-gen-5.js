  let hexDigitPrimes = new Set([2, 3, 5, 7, 11, 13]);
  let count = 0;

  for (let i = 0; i < num.length; i++) {
    let hexDigit = parseInt(num[i], 16);
    if (hexDigitPrimes.has(hexDigit)) count++;
  }

  return count;
};

console.log(hexKey("AB")); // 1
console.log(hexKey("1077E")); // 2
console.log(hexKey("ABED1A33")); // 4
console.log(hexKey("123456789ABCDEF0")); // 6
console.log(hexKey("2020")); // 2

//The solution works by converting each hexadecimal digit to decimal,
//and checking if the decimal value is in the set of known prime hexadecimal digits.
//If it is, we increment our count. At the end of the function, we return the count.
```

This solution has a time complexity of O(n), where n is the length of the input string.

The space complexity is O(1), since we are using a constant amount of space to store the prime hexadecimal digits.

This solution assumes that the input string is always correct or an empty string and that the hexadecimal digits are always uppercase.

If you have any questions, feel free to ask.

-[Nitin](https://www.linkedin.com/in/nitin-jain-775a3b1a6/)

```



```python
def hexKey(num):
    hexDigitPrimes = {2, 3, 5, 7, 11, 13}
    count = 0

    for i in num:
        hexDigit = int(i, 16)
        if hexDigit in hexDigitPrimes:
            count += 1

    return count

print(hexKey("AB")) # 1
print(hexKey("1077E")) # 2