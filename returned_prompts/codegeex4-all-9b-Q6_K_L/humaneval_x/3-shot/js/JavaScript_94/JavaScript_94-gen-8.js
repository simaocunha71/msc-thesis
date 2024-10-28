  const isPrime = (num) => {
    if (num <= 1) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;
    for (let i = 3; i <= Math.sqrt(num); i += 2) {
      if (num % i == 0) return false;
    }
    return true;
  }

  const largestPrime = (lst) => {
    let largest = -1;
    for (const num of lst) {
      if (isPrime(num) && num > largest) {
        largest = num;
      }
    }
    return largest;
  }

  if (lst.length == 0) {
    return 0;
  } else {
    let prime = largestPrime(lst);
    let digits = prime.toString().split('');
    let sum = 0;
    for (const digit of digits) {
      sum += parseInt(digit);
    }
    return sum;
  }
}



