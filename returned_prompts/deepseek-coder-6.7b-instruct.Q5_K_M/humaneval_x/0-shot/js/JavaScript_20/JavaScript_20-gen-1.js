  numbers.sort((a, b) => a - b);
  let minDiff = Infinity;
  let result = [];

  for(let i = 0; i < numbers.length - 1; i++){
    const diff = numbers[i + 1] - numbers[i];
    if(diff < minDiff){
      minDiff = diff;
      result = [numbers[i], numbers[i + 1]];
    }
  }
  return result;
};

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]));  //(2.0, 2.2)
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]));  //(2.0, 2.0)

```

The function `findClosestElements` sorts the array in ascending order. Then it iterates over the array, calculating the difference between each number and its successor. If this difference is smaller than the current minimum difference `minDiff`, it updates `minDiff` and `result` with the current pair of numbers. Finally, it returns `result`.

This approach has a time complexity of O(n log n) due to the sorting operation.

The space complexity is O(1) because no additional space is used that scales with the size of the input.
*/

const findClosestElements = (numbers) => {
  numbers.sort((a, b) => a - b);
  let minDiff = Infinity;
  let result = [];

  for(let i = 0; i < numbers.length - 1; i++){
    const diff = numbers[i + 1] - numbers[i];
    if(diff < minDiff){
      minDiff = diff;
      result = [numbers[i], numbers[i + 1]];
    }
  }
  return result;
};

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 