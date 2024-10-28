  let prime = (n) => {
    if (n < 2) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  }

  let maxPrime = -Infinity;
  for (let i = 0; i < lst.length; i++) {
    if (prime(lst[i]) && lst[i] > maxPrime) {
      maxPrime = lst[i];
    }
  }

  if (maxPrime === -Infinity) return 0;

  return Array.from(maxPrime.toString()).reduce((a, b) => a + +b, 0);
}

// Testing
console.log(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])); // 10
console.log(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1])); // 25
console.log(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3])); // 13
console.log(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6])); // 11
console.log(skjkasdkd([0,81,12,3,1,21])); // 3
console.log(skjkasdkd([0,8,1,2,1,7])); // 7

// Please comment your code to explain the steps.

// The function 'prime' checks if