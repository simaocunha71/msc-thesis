  if(n < 0)
    return 'Invalid Input';
  if(n === 0 || n === 1)
    return 0;
  if(n === 2)
    return 2;
  if(n === 3)
    return 0;

  let fib = [0, 0, 2, 0];

  for(let i = 4; i <= n; i++){
    fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4];
  }

  return fib[n];
}

console.log(fib4(5)); // 4
console.log(fib4(6)); // 8
console.log(fib4(7)); // 14

This solution is iterative, so its time complexity is O(n). It also uses an array to store the previously computed fib4 values, so its space complexity is O(n).
The function first handles the base cases for n=0, n=1, n=2 and n=3. Then it initializes an array with the first four values of the fib4 sequence. After that it computes the n-th value in a loop and stores it in the array. The n-th value is then returned.

Alternatively, you can use a constant space solution with time complexity of O(n):

const fib4 = (n) => {
  if(n < 0)
    return 'Invalid Input';
  if(n === 0 || n === 1)
    return 0;
  if(n === 2)
    return 2;
  if(n === 3)
    return 0;

  let a = 0, b = 0, c = 2, d = 0;

  for(let i = 4; i <= n; i++){
    let temp = d;
    d = a + b + c + d;
    a = b;
    b = c;
    c = temp;
  }

  return d;
}

In this solution, we use four variables to keep track of the last four values in the fib4 sequence. The new value is computed by adding the last four values and then the