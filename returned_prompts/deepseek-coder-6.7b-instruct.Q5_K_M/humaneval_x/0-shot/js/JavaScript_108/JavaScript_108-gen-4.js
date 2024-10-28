  let count = 0;
  for(let i = 0; i < arr.length; i++){
    if(sumDigits(arr[i]) > 0){
      count++;
    }
  }
  return count;
}

const sumDigits = (num) => {
  let sum = 0;
  const numStr = num.toString();
  for(let i = 0; i < numStr.length; i++){
    sum += Number(numStr[i]);
  }
  return sum;
}
console.log(countNums([]) == 0)
console.log(countNums([-1, 11, -11]) == 1)
console.log(countNums([1, 1, 2]) == 3)

This function countNums loops through the array and for each number, it calculates the sum of its digits by calling the helper function sumDigits. If the sum is greater than 0, it increments the count. Finally, it returns the count.

The helper function sumDigits converts the number into a string and loops through each character (digit) in the string, adding them to the sum. It then returns the sum.
*/

// Solution:
function countNums(arr) {
  let count = 0;
  for(let i = 0; i < arr.length; i++){
    if(sumDigits(arr[i]) > 0){
      count++;
    }
  }
  return count;
}

function sumDigits(num) {
  let sum = 0;
  const numStr = num.toString();
  for(let i = 0; i < numStr.length; i++){
    sum += Number(numStr[i]);
  }
  return sum;
}
console.log(countNums([]) == 0)
console.log(countNums([-1, 11, -11]) == 1)
console.log(countNums([1, 1, 2]) == 3)
```

The above solution is written in JavaScript. It defines two functions `countNums` and `sumDigits`. The `countNums`