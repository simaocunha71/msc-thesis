  let max = 0;
  let max_prime_digits = 0;
  for (let i = 0; i < lst.length; i++) {
    let prime = true;
    for (let j = 2; j < lst[i]; j++) {
      if (lst[i] % j === 0) {
        prime = false;
        break;
      }
    }
    if (prime) {
      if (lst[i] > max) {
        max = lst[i];
        max_prime_digits = 0;
      }
      max_prime_digits += lst[i];
    }
  }
  return max_prime_digits;
};



