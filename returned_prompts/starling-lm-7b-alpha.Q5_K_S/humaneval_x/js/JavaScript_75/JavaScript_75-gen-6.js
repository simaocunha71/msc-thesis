  function isPrime(num) {
    if (num < 2) return false;
    for (let i = 2; i * i <= num; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  let arr = [];
  for (let i = 2; i < 100; i++) {
    if (isPrime(i)) {
      arr.push(i);
    }
  }

  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      for (let k = 0; k < arr.length; k++) {
        if (arr[i] * arr[j] * arr[k] === a) {
          return true;
        }
      }
    }
  }

  return false;
}



