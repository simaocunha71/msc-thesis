  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    let num = arr[i];
    if (num < 0) {
      num = num * -1;
      while (num > 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
      }
      if (sum > 0) count++;
    } else {
      while (num > 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
      }
      if (sum > 0) count++;
    }
  }
  return count;
};

console.log(countNums([]));  // 0
console.log(countNums([-1, 11, -11]));  // 1
console.log(countNums([1, 1, 2]));  // 3
```


## 6. Sorting and Filtering

