/*
The problem asks to return the product of the odd digits.

The solution I have is to use a loop to go through each digit.
If the digit is odd, multiply it by the result of the previous loop.
If the digit is even, return 0.

*/
  let result = 1;
  for (let i=0; i<n.toString().length; i++) {
    if (n.toString()[i] % 2 === 0) {
      return 0;
    }
    result *= n.toString()[i];
  }
  return result;
}

/*


*/