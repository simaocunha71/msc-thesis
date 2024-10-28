  let count = 0;

  for(let i = 0; i < arr.length; i++) {
    let sum = 0;
    let num = arr[i];
    if(num < 0) {
      num = num * -1;
      while(num > 0) {
        let digit = num % 10;
        sum += digit * -1;
        num = Math.floor(num / 10);
      }
    } else {
      while(num > 0) {
        let digit = num % 10;
        sum += digit;
        num = Math.floor(num / 10);
      }
    }

    if(sum > 0) {
      count++;
    }
  }

  return count;
};

console.log(countNums([]));
console.log(countNums([-1, 11, -11]));
console.log(countNums([1, 1, 2]));
// 0, 1, 3
```


### Python
```python
