  let count = 0;
  for (let i of arr) {
    let sum = 0;
    let isNegative = i < 0;
    if (isNegative) {
      i = -i;
    }
    while (i > 0) {
      sum += i % 10;
      i = Math.floor(i / 10);
    }
    if (sum > 0) {
      count++;
    }
  }
  return count;
}  // 1. Get the sum of digits for each number in the array
    // 2. If the sum of digits is greater than 0, increment the count
    // 3. Return the count
}  // This is not a very efficient solution as it involves converting each number to string to get the digits. It can be optimized to avoid this conversion.