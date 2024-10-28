  if (l.length === 0) return true;

  let increase = true;
  let decrease = true;

  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] > l[i + 1]) increase = false;
    if (l[i] < l[i + 1]) decrease = false;
  }

  return increase || decrease;
}

console.log(monotonic([1, 2, 4, 20])) // true
console.log(monotonic([1, 20, 4, 10])) // false
console.log(monotonic([4, 1, 0, -10])) // true

```



## 8. Write a function called `largest` that takes an array of numbers and returns the largest number in the array. 

