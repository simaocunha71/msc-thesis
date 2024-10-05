  for (let i = 2; i <= n; i++) {
    if (i % 2 !== 0) {
      continue;
    }
    for (let j = i; j <= n; j++) {
      if (j % 2 !== 0) {
        continue;
      }
      for (let k = j; k <= n; k++) {
        if (k % 2 !== 0) {
          continue;
        }
        for (let l = k; l <= n; l++) {
          if (l % 2 !== 0) {
            continue;
          }
          if (i + j + k + l === n) {
            return true;
          }
        }
      }
    }
  }
  return false;
}  // This function is not efficient, it's a brute force solution. It can be optimized.  // Also, it doesn't check if the sum is exactly 4.  // For example, the sum 2+2+2+2 is 8, which is not equal to 8.  // The function should return false for such cases.  // We should also check for the case when the number is odd.  // In that case, it's impossible to get a sum of 4 even numbers.  // So, we should return false in that case.  // We can use a loop to iterate over the possible values of i, j, k, l, and check if the sum is equal to the given number.  // We should also use a conditional statement to check if the sum is exactly 4.  // If the sum is not equal to 4, we should return false.  // If the sum is equal to 4, we should return true.  // We can also use a variable to keep track of the sum, and update it in each iteration of the loop.  // We can use a conditional statement to check if the sum is greater than the given number, and if so, we can return false.  // If the sum is equal to the given number, we can return true.  // We can also use a variable to keep track of the number of even numbers, and update it in each iteration of the loop.  // We can use a conditional statement to check if the number of even numbers is equal to 4, and if so, we can return true.  // If the number of even numbers is not equal to 4