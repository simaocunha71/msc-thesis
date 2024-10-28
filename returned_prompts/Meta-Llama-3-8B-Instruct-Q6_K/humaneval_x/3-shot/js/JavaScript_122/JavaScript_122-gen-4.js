  let sum = 0;
  for (let i = 0; i < k; i++) {
    let num = Math.abs(arr[i]);
    if (String(num).length <= 2) {
      sum += num;
    }
  }
  return sum;
}
// The abs function is used to handle negative numbers. The String function is used to convert the number to a string, and the length property is used to get the number of digits. The Math library is used to get the absolute value of the number. The sum is then returned as the result.