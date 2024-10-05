
// Create an array to store the Fib4 numbers.
  fib_nums := make([]int, n+1)

  // Set the first two Fib4 numbers.
  fib_nums[0], fib_nums[1], fib_nums[2], fib_nums[3] = 0, 0, 2, 0

  // Compute the rest of the Fib4 numbers.
  for i := 4; i <= n; i++ {
    fib_nums[i] = fib_nums[i-1] + fib_nums[i-2] + fib_nums[i-3] + fib_nums[i-4]
  }

  // Return the n-th Fib4 number.
  return fib_nums[n]
}

// This function uses dynamic programming to compute the n-th Fib4 number. 
// It stores the computed Fib4 numbers in an array and uses this array to compute the next Fib4 number.
// This avoids the need for recursion and makes the function more efficient.

```

This is the Python version of the same code:

```python

def Fib4(n):
  # Create an array to store the Fib4 numbers.
  fib_nums = [0]*(n+1)

  # Set the first two Fib4 numbers.
  fib_nums[0], fib_nums[1], fib_nums[2], fib_nums[3] = 0, 0, 2, 0

  # Compute the rest of the Fib4 numbers.
  for i in range(4, n+1):
    fib_nums[i] = fib_nums[i-1] + fib_nums[i-2] + fib_nums[i-3] + fib_nums[i-4]

  # Return the n-th Fib4 number.
  return fib_nums[n]

```

Both codes do the same thing: they compute the n-th Fib4 number by summing the previous four numbers in the sequence. The difference is in the syntax and the programming language used.