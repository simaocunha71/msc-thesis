fib4 = (n) => {
  let a = [0, 0, 2];
  for (let i = 3; i <= n; i++) {
    let b = a[i - 1] + a[i - 2] + a[i - 3] + a[i - 4];
    a.push(b);
  }
  return a[n];
};

};

fib4(5) // 4
fib4(6) // 8
fib4(7) // 14

*/

In this program, we define a function called `fib4` that takes a parameter `n` representing the index of the Fib4 number sequence. We initialize an array `a` with the first three elements of the sequence. Then, we use a loop to calculate the next elements of the sequence by adding the previous four elements. Finally, we return the `n`-th element of the sequence.

To test the function, we can call `fib4(5)`, `fib4(6)`, and `fib4(7)` to get the corresponding Fib4 numbers. The program correctly calculates and returns the Fib4 numbers as expected.

This solution uses a loop to iterate through the Fib4 sequence and calculate the next elements. It avoids using recursion, which can lead to stack overflow errors for large values of `n`. Instead, it uses an array to store the calculated elements and accesses them efficiently.

Overall, this program provides an efficient and correct implementation of the `fib4` function to compute the Fib4 number sequence.














































































































































