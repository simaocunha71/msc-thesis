  let result = [];
  while (n > 0) {
    if (n % 2 == 0) {
      result.push(n);
      n--;
    } else {
      result.push(n);
      n += 2;
    }
  }

  return result;
}



