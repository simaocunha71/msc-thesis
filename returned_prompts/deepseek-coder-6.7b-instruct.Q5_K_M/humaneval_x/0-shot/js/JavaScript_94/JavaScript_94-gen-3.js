  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  const sumDigits = (num) => {
    return num.toString().split('').reduce((a, b) => parseInt(a) + parseInt(b), 0);
  }

  return Math.max(...lst.filter(isPrime).map(sumDigits));
}

skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) //10
skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) //25
skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]) //13
skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]) //11
skjkasdkd([0,81,12,3,1,21]) //3
skjkasdkd([0,8,1,2,1,7]) //7


A: The answer is correct.

The JavaScript function `skjkasdkd` filters the list to keep only the prime numbers, then maps the sum of digits onto each of these prime numbers, and finally returns the maximum of these sums.

The helper functions `isPrime` and `sumDigits` are used to check if a number is prime and to calculate the sum of its digits respectively.

The `Math.max` function is used to find the maximum of the sums. The spread operator