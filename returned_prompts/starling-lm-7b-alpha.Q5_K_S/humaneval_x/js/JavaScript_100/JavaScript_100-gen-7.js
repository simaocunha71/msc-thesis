  let result = [];
  while (n > 0) {
    result.push(n);
    if (n % 2 == 0) {
      n += 2;
    } else {
      n += 1;
    }
  }

  return result;
}



