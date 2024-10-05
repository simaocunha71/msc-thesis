  let result = y;

  if (n > 1) {
    for (let i = 2; i < n; i++) {
      if (n % i === 0) {
        result = x;
        break;
      }
    }
  }

  return result;
}

