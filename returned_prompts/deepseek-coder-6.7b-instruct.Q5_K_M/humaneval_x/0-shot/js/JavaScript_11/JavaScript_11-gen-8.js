  let result = "";
  for (let i = 0; i < a.length; i++) {
    result += (a[i] ^ b[i]) + "";
  }
  return result;
};

console.log(stringXor('010', '110')); // '100'

/*
  This program takes two binary strings as inputs. 
  It performs an XOR operation on each pair of corresponding digits from the two strings.
  The result is a new string that consists of the XOR results of the corresponding digits from the original strings.
*/
```

##### Explanation:
The `stringXor` function performs a binary XOR operation on each pair of corresponding digits from the two input strings. This is done by using a `for` loop to iterate over each character in the strings. The `^` operator is used to perform the XOR operation. The result of the XOR operation is converted to a string and appended to the `result` string. The function finally returns the `result` string.

In the example given, `stringXor('010', '110')` returns '100'. This is because the XOR operation of the corresponding digits in `010` and `110` is performed as follows: 0 XOR 1 is 1, 1 XOR 1 is 0, and 0 XOR 0 is 0.

Note that this function assumes that the input strings `a` and `b` are of the same length. If this is not the case, the function will not work correctly.

Also note that this function uses the JavaScript `^` operator for XOR operation. The `^` operator in JavaScript performs a bitwise XOR operation on two numbers.

```javascript
console.log(stringXor('010', '110')); // '100'
```

In this example, `stringXor('010', '110')` returns '100'. This is because the XOR operation of the corresponding digits in `010` and `110` is performed as follows: 0 XOR 1 is 1, 1 XOR 1 is 0, and 0