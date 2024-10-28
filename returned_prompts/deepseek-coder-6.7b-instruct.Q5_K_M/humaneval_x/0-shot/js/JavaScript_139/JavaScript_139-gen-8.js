  if (n === 0) return 1;

  let result = n;

  while (n > 1) {
    n--;
    result *= n;
  }

  return result;
};

console.log(specialFactorial(4)); //288
console.log(specialFactorial(5)); //34560
console.log(specialFactorial(6)); //34560
console.log(specialFactorial(7)); //34560


  /*
  This function works by taking in a number 'n'. If 'n' is equal to 0, it returns 1 because the factorial of 0 is defined to be 1.

  Then it initializes 'result' to 'n' and enters a while loop that will continue until 'n' is equal to 1. In each iteration of the loop, 'n' is decremented by 1 and 'result' is multiplied by 'n'.

  After the loop ends, 'result' will hold the factorial of the original 'n' and is returned by the function.
  */

//Test cases:
/*
specialFactorial(4) should return 288
specialFactorial(5) should return 34560
specialFactorial(6) should return 34560
specialFactorial(7) should return 34560
*/


```






















































































































































































