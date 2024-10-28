```javascript
const sortNumbers = (numbers) => {
  const numMap = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
  };
  const nums = numbers.split(' ').map(num => numMap[num]).sort((a, b) => a - b).map(num => Object.keys(numMap).find(key => numMap[key] === num));
  return nums.join(' ');
};

console.log(sortNumbers('three one five')); // Output: "one three five"
```

The function `sortNumbers` takes a space-delimited string of numbers as an argument. It first defines a map `numMap` that maps each number to its corresponding integer value. It then splits the input string into an array of numbers, maps each number to its corresponding integer value, sorts the array, and finally maps each integer value back to its corresponding number. The resulting array of numbers is then joined back into a string with spaces in between and returned. The `Object.keys` method is used to find the key in the `numMap` object that corresponds to each integer value. The `sort` method is used to sort the array of numbers in ascending order. The `map` method is used to transform the array of numbers into an array of strings. The `join` method is used to join the array of strings back into a string with spaces in between. 

When the function is called with the input 'three one five', it returns the string 'one three five', which is the input string with the numbers sorted from smallest to largest. 