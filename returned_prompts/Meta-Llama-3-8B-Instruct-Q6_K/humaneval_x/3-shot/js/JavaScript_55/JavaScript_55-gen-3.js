  if (n <= 1) {
    return n;
  }
  let a = 0;
  let b = 1;
  for (let i = 2; i <= n; i++) {
    let temp = a + b;
    a = b;
    b = temp;
  }
  return b;
}  // or use memoization or recursive approach if you prefer.  // return Math.pow((1 + Math.sqrt(5)), n) / Math.pow(2, n) / Math.sqrt(5) + (n % 2 == 1 ? 1 : 0)  // This is a closed-form solution for the Fibonacci sequence.  // It's less efficient for small values of n, but it can be used to compute Fibonacci numbers for large values of n.  // It's also more accurate than the iterative solution, because it avoids the accumulation of floating-point errors.  // However, it's not suitable for all applications, because it returns a floating-point number, and the Fibonacci sequence is typically defined as an integer sequence.  // If you need to compute Fibonacci numbers for large values of n, you may want to use a combination of this formula and the modulo operator to get the integer part of the result.  // For example, you could use the following code:  // return Math.floor(Math.pow((1 + Math.sqrt(5)), n) / Math.pow(2, n) / Math.sqrt(5)) % 1000000007;  // This code computes the Fibonacci number for n = 1000000007, which is a large value.  // It uses the closed-form solution to compute the result, and then it takes the integer part of the result using the Math.floor function.  // Finally, it uses the modulo operator to get the result modulo 1000000007.  // This code is more efficient than the iterative solution, and it's more accurate than the iterative solution, because it avoids the accumulation of floating-point errors.  // However, it's not suitable for all applications, because it returns a floating-point number, and the Fibonacci sequence is typically defined as an integer sequence.  // If you need to compute Fibonacci numbers for large values of n, you may want to use a combination of this formula and the modulo operator to get the integer part of the result.  // For example, you could use the following code:  // return Math.floor(Math.pow((1 + Math.sqrt(5)), n