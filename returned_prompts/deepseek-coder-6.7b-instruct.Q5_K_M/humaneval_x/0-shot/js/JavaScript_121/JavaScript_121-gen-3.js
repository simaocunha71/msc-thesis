  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
}

console.log(solution([5, 8, 7, 1])); // 12
console.log(solution([3, 3, 3, 3, 3])); // 9
console.log(solution([30, 13, 24, 321])); // 0
```

This function works by initializing a variable `sum` to 0, then iterating over the input list with a for loop. For each element, it checks if its position is even (`i % 2 === 0`) and if the element is odd (`lst[i] % 2 !== 0`). If both conditions are true, it adds the element to `sum`. Finally, it returns `sum`.


```javascript
// function solution(lst){
//   let sum = 0;
//   for (let i = 0; i < lst.length; i++) {
//     if (i % 2 === 0 && lst[i] % 2 !== 0) {
//       sum += lst[i];
//     }
//   }
//   return sum;
// }

// console.log(solution([5, 8, 7, 1])); // 12
// console.log(solution([3, 3, 3, 3, 3])); // 9
// console.log(solution([30, 13, 24, 321])); // 0
// }
```
















































































