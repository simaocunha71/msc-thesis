  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
} // This function is not very efficient for large values of n. It could be improved with a formula. The sum of all numbers up to n is n*(n+1)/2. So the function could be written as sumToN = n => n * (n + 1) / 2; // This function will work correctly for any positive integer n.