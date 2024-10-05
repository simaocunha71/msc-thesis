  let a = 1, b = 1, count = 1;

  while (count < n) {
    let temp = a + b;
    a = b;
    b = temp;
    if (isPrime(b)) {
      count++;
    }
  }

  return b;
}

const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
}
```

The above code defines five functions, each with its own problem and solution. The functions are:

1. `hasCloseElements`: This function checks if there are any two numbers in the given list that are closer to each other than the given threshold.
2. `separateParenGroups`: This function separates a string of nested parentheses into separate groups.
3. `truncateNumber`: This function returns the decimal part of a given positive floating-point number.
4. `primeFib`: This function returns the n-th number that is both a Fibonacci number and a prime number.
5. `isPrime`: This is a helper function used by `primeFib` to check if a number is prime.

The functions are implemented using JavaScript and are tested using the provided unit tests. The `isPrime` function is a helper function used by `primeFib` to check if a number is prime.

The `hasCloseElements` function uses two nested loops to check each pair of numbers in the list. The `separateParenGroups` function uses a single loop to iterate over the input string, and it keeps track of the current group being processed using a stack.

The `truncateNumber` function simply returns the remainder of the division of the input number by 1.0, which is the decimal part of the number.

The `primeFib` function uses a loop to generate Fibonacci numbers and checks each number to see if it is prime using the `isPrime` function. The first number that is both a Fibonacci number and a prime number is returned.

The `isPrime` function checks if a number is prime by checking if it is divisible by any number up to its square root. If it is not divisible by any of these numbers, it is prime.