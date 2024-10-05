  if(lst.length === 0){
    return 0;
  }
  let sum = 0;
  for(let i = 0; i < lst.length; i++){
    if(lst[i] > 0 && lst[i] % 2 === 1){
      sum += Math.pow(lst[i], 2);
    }
  }
  return sum;
}

console.log(doubleTheDifference([1, 3, 2, 0])); //10
console.log(doubleTheDifference([-1, -2, 0])); //0
console.log(doubleTheDifference([9, -2])); //81
console.log(doubleTheDifference([0])); //0
console.log(doubleTheDifference([])); //0

```

## 3. Write a JavaScript function that takes two arrays of numbers, and returns the sum of the numbers in the arrays that are odd and greater than 5.

```javascript

