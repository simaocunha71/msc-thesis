  if(n < 2) return 0;
  if(n === 2) return 1;

  let fib = [0, 0, 1];

  for(let i = 3; i <= n; i++) {
    fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
  }

  return fib[n];
};

console.log(fibfib(1)); // 0
console.log(fibfib(5)); // 4
console.log(fibfib(8)); // 24

```

This function first handles the base cases of the sequence. Then it initializes an array with the first three numbers of the sequence. The function then loops from 3 to n and at each step it calculates the next number in the sequence by adding together the previous three numbers. Finally, it returns the nth number in the sequence.

The time complexity of this function is O(n) and the space complexity is O(n) as well because it stores the whole sequence up to the nth number. This makes it efficient for large n.

This function uses a bottom-up approach to compute the n-th FibFib number by starting with the base cases and gradually building up to the n-th number. This approach is more efficient than a top-down recursive approach that could result in a large number of function calls and potentially stack overflow errors for large n.

```javascript

