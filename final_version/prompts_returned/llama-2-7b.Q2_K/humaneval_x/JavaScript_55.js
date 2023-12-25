/*Return n-th Fibonacci number.
  >>> fib(10)
  55
  >>> fib(1)
  1
  >>> fib(8)
  21
  */
const fib = (n) => {
  let fibNumber = 0;
  if (arguments.length != 1) throw new Error('Please, pass the number.');
  for (let i = 1; i <= n; i++) {
    const temp = Math.pow(i, 2);
    fibNumber += ((fibNumber + Math.sqrt(temp)) / Math.sqrt(temp));
  }
  return fibNumber;
};

module.exports = fib;
