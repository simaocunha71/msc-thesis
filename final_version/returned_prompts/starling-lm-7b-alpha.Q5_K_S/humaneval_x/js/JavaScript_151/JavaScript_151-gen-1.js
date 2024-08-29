  let result = 0;
  for (const n of lst) {
    if (n % 1 === 0 && n >= 0 && n % 2 !== 0) {
      result += n*n;
    }
  }
  return result;
}



