  let result = 0;
  for (const n of lst) {
    if (n % 1 === 0 && n >= 0 && n % 2 === 1) {
      result += n * n;
    }
  }
  return result;
}



