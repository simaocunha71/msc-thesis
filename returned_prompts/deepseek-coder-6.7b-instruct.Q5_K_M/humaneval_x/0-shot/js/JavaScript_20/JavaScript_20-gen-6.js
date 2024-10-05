let min_diff = Number.MAX_VALUE;
  let result = [0, 0];
  numbers.sort((a, b) => a - b);
  for (let i = 0; i < numbers.length - 1; i++) {
    if (numbers[i + 1] - numbers[i] < min_diff) {
      min_diff = numbers[i + 1] - numbers[i];
      result = [numbers[i], numbers[i + 1]];
    }
  }
  return result;
}

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]));
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]));

This function will take an array of numbers and return two numbers that are closest to each other. It does this by first sorting the array in ascending order. Then it iterates over the sorted array comparing the difference between adjacent elements. If the difference is less than the current minimum difference, it updates the minimum difference and the pair of numbers. Finally, it returns the pair of numbers with the smallest difference.
<jupyter_output>
<empty_output>
<jupyter_text>
