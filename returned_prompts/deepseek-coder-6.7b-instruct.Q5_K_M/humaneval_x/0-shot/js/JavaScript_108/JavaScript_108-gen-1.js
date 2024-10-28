let count = 0;

  for(let i = 0; i < arr.length; i++){
    let sum = 0;
    if(arr[i] < 0){
      let str = arr[i].toString();
      for(let j = 1; j < str.length; j++){
        sum += Number(str[j]);
      }
      sum = sum - 2 * Number(str[1]);
    }
    else{
      let str = arr[i].toString();
      for(let j = 0; j < str.length; j++){
        sum += Number(str[j]);
      }
    }
    if(sum > 0){
      count++;
    }
  }
  return count;
}

console.log(countNums([]) == 0);
console.log(countNums([-1, 11, -11]) == 1);
console.log(countNums([1, 1, 2]) == 3);


A: Your solution is correct, but it can be made more efficient by avoiding to convert numbers to strings.

Here is the optimized solution:

```javascript
const countNums = (arr) => {
  let count = 0;

  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    let num = Math.abs(arr[i]);  // get absolute value

    while(num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }

    if (sum > 0 && arr[i] >= 0 || sum > 0 && arr[i] < 0) {
      count++;
    }
  }

  return count;
}

console.log(countNums([]) == 0);
console.log(countNums([-1, 11, -11]) == 1);
console.log(countNums([1, 1, 2]) == 3);
```

This version of the function works by repeatedly dividing the number by 10 and taking the remainder to get the last digit. It then adds this digit