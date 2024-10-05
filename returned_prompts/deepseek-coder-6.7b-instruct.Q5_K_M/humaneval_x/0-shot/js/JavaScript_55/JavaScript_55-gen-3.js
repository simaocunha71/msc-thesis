  if (n <= 2) return 1;
  let fibNums = [1, 1];
  for (let i = 2; i < n; i++) {
    fibNums.push(fibNums[i - 1] + fibNums[i - 2]);
  }
  return fibNums.pop();
}

console.log(fib(10)); // 55
console.log(fib(1)); // 1
console.log(fib(8)); // 21

*/


A: The fib function calculates the nth Fibonacci number. It uses an array called fibNums to store the calculated Fibonacci numbers. The first two Fibonacci numbers are always 1, so the array is initialized with these two numbers. The function then enters a loop that calculates the remaining Fibonacci numbers up to the nth one. In each iteration of the loop, the function adds the last two numbers in the fibNums array together and pushes the result onto the array. After the loop finishes, the function returns the last number in the fibNums array, which is the nth Fibonacci number.

The console.log statements at the end of the code are used to test the fib function. They call the function with different arguments and log the results to the console. The expected results are given in the problem statement.

Overall, this code is correct and should work as expected.

*/

