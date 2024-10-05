  let prime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  let maxPrime = Math.max(...lst.filter(prime));
  return maxPrime.toString().split('').reduce((a, b) => a + +b, 0);
}

console.log(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])); // 10
console.log(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1])); // 25
console.log(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3])); // 13
console.log(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6])); // 11
console.log(skjkasdkd([0,81,12,3,1,21])); // 3
console.log(skjkasdkd([0,8,1,2,1,7])); // 7

/*
The function skjkasdkd filters out prime numbers from the array using the function prime.
Then it finds the maximum prime number using the function Math.max and the spread operator.
Finally, it turns the maximum prime number into a string, splits it into an array of digits,
and reduces the array to the sum of its elements by adding up the digits.
*/
```

## Code Explanation:

1. The function `prime