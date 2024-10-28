  let result = [1, 3];
  for (let i = 2; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(1 + i / 2);
    } else {
      let a = result[i - 1];
      let b = result[i - 2];
      let c = result[i - 3];
      result.push(a + b + c);
    }
  }
  return result;
}  // This function will return the first n+1 numbers of the Tribonacci sequence. It first creates a list of the first two numbers of the sequence and then uses a loop to calculate the next numbers based on the recurrence relation. The loop checks if the current number is even or odd to determine whether to use the simple formula or the recursive formula.