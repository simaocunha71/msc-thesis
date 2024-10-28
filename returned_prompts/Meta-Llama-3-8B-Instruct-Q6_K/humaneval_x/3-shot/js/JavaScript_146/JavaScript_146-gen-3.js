  let count = 0;
  for (let num of nums) {
    if (num > 10 && Math.floor(Math.abs(num) / 10) % 2 !== 0 && num % 10 % 2 !== 0) {
      count++;
    }
  }
  return count;
}  // Time Complexity: O(n), where n is the number of elements in the array. Space Complexity: O(1).