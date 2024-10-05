  let count = 0;

  arr.forEach((num) => {
    let sum = 0;
    let strNum = String(Math.abs(num));

    for (let i = 0; i < strNum.length; i++) {
      sum += Number(strNum[i]);
    }

    if (num < 0) {
      sum *= -1;
    }

    if (sum > 0) {
      count++;
    }
  });

  return count;
};

console.log(countNums([]) == 0);
console.log(countNums([-1, 11, -11]) == 1);
console.log(countNums([1, 1, 2]) == 3);
```

## Answer 11

```javascript
