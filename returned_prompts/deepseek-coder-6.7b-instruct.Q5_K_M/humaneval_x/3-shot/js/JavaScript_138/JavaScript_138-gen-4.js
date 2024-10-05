  let count = 0;
  for (let i = 2; i < n; i += 2) {
    if (n - i >= 0) {
      count++;
      n -= i;
    } else {
      break;
    }
  }
  return count === 4 && n % 2 === 0;
}



