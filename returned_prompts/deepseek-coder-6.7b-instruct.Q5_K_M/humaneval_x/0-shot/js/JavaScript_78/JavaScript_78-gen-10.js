  const primeHexadecimal = ['2', '3', '5', '7', 'B', 'D'];
  let count = 0;

B:
  for (let i = 0; i < num.length; i++) {
    if (primeHexadecimal.includes(num[i])) {
      count++;
    }
  }

C:
  return count;
};

module.exports = hexKey;

*/

const hexKey = (num) => {
  const primeHexadecimal = ['2', '3', '5', '7', 'B', 'D'];
  let count = 0;

  for (let i = 0; i < num.length; i++) {
    if (primeHexadecimal.includes(num[i])) {
      count++;
    }
  }

  return count;
};

module.exports = hexKey;

/*
Test.assertEquals(hexKey("AB"),1)
Test.assertEquals(hexKey("1077E"),2)
Test.assertEquals(hexKey("ABED1A33"),4)
Test.assertEquals(hexKey("123456789ABCDEF0"),6)
Test.assertEquals(hexKey("2020"),2)
*/
```

## JavaScript

```javascript
/*
