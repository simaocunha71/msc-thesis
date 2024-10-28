  let count = 0;

  for(let i = 0; i < arr.length; i++) {
    let num = arr[i];
    let sum = 0;

    while(num != 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }

    if(sum > 0) {
      count++;
    }
  }

  return count;
};

console.log(countNums([])); // 0
console.log(countNums([-1, 11, -11])); // 1
console.log(countNums([1, 1, 2])); // 3
```

This solution works by first initializing a count variable to 0. This variable will keep track of how many numbers in the array have a sum of digits greater than 0.

The solution then iterates through each number in the array. For each number, it calculates the sum of its digits by taking the modulo 10 of the number and adding this to a sum variable. It then takes the floor division of the number by 10 to remove the last digit from the number. This process is repeated until there are no more digits left in the number.

If the sum of the digits is greater than 0, the count is incremented by 1.

Finally, the function returns the count.

The time complexity of this solution is O(n*m), where n is the number of elements in the array and m is the number of digits in the largest number in the array. This is because for each number in the array, the function iterates through all of its digits. The space complexity is O(1), as the function only uses a constant amount of space to store the count and the sum of digits.

This solution assumes that the input array will only contain integers. If the input array can contain non-integer elements, the function should be modified to handle this case.

If you have any questions about this solution, please let me know.
*/

const countNums = (arr) => {
  let count = 0;

  for(let i = 0; i < arr.length; i++) {
