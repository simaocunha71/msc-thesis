  let result = 2;

  while (n % 2 === 0) {
    result = 2;
    n /= 2;
  }

  for (let i = 3; i * i <= n; i += 2) {
    while (n % i === 0) {
      result = i;
      n /= i;
    }
  }

  if (n > 2) {
    result = n;
  }

  return result;
}



