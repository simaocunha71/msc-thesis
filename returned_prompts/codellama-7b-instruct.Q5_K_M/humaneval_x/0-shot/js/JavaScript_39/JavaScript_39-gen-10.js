  let prime = (n) => {
    for (let i = 2; i < n; i++) {
      if (n % i === 0) return false;
    }
    return n > 1;
  };

  let fib = (n) => {
    let a = 0, b = 1;
    for (let i = 0; i < n; i++) {
      [a, b] = [b, a + b];
    }
    return a;
  };

  for (let i = 0; i < n; i++) {
    let num = fib(i);
    if (prime(num)) return num;
  }

  return 1;
};

