  let length = string.length;
  let i = 2;

  while (i * i <= length) {
    if (length % i === 0) {
      return false;
    }
    i++;
  }
  return true;
};

// You can use the above function to test:
console.log(primeLength('Hello'));       // true
console.log(primeLength('abcdcba'));     // true
console.log(primeLength('kittens'));     // true
console.log(primeLength('orange'));      // false



/*
Explanation:
The function primeLength takes in a string as an argument and first determines the length of the string. It then initializes a variable i to 2.

Next, the function enters a while loop that continues as long as i * i is less than or equal to the length of the string. This loop is used to check if the length of the string is divisible by any number between 2 and the square root of the length.

Within the loop, the function checks if the length of the string is divisible by i using the modulus operator (%). If the length is divisible by i, it means that the length is not a prime number, so the function returns false.

If the loop completes without finding a divisor for the length of the string, the function returns true, indicating that the length is a prime number.

The provided test cases demonstrate the usage of the primeLength function and show the expected output for different inputs.

In the first test case, 'Hello' has a length of 5, which is a prime number, so the function returns true.

In the second test case, 'abcdcba' has a length of 7, which is also a prime number, so the function returns true.

In the third test case, 'kittens' has a length of 7, which is a prime number, so the function returns true.

In the fourth test case, 'orange' has a length of 6, which is not a prime number (as it is divisible by 2 and 3), so the function returns false.

By using the primeLength function and testing it with different inputs, you can determine if the length of a string is a prime number or