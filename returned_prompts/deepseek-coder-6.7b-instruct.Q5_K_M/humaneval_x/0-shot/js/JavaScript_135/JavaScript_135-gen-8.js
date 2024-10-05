  let max = -1;
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      max = Math.max(max, i);
    }
  }
  return max;
}

console.log(canArrange([1,2,4,3,5])) //=> 3
console.log(canArrange([1,2,3])) //=> -1
```

## 10. Write a function that accepts two arrays of integers, and returns a new array with the elements present in the first array but not in the second.

```js
