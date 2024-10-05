  let count = 0;
  for (let num of arr) {
    if (Math.abs(num) > 0) {
      let sum = 0;
      let str = Math.abs(num).toString();
      for (let i = 0; i < str.length; i++) {
        sum += parseInt(str[i]);
      }
      if (sum > 0) {
        count++;
      }
    }
  }
  return count;
}
```



