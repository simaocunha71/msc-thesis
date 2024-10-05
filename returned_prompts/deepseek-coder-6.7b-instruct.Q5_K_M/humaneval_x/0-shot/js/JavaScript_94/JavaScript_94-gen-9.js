  const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if (num % i === 0) return false;
    return true;
  }

  const sumDigits = (num) => {
    return num.toString().split('').reduce((a, b) => parseInt(a) + parseInt(b), 0);
  }

  return Math.max(...lst.filter(isPrime).map(sumDigits));
}

skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]);
skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]);
skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]);
skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]);
skjkasdkd([0,81,12,3,1,21]);
skjkasdkd([0,8,1,2,1,7]);

I:
I think the problem can be solved by first filtering out the prime numbers in the given list using the helper function isPrime. Then, we map over the filtered list and use the helper function sumDigits to calculate the sum of the digits for each prime number. Finally, we return the maximum of these sums.

The helper function isPrime uses a for loop to check if a number is prime. If the number is less than 2, it returns false. If the number is greater than or equal to 2, it checks if it is div