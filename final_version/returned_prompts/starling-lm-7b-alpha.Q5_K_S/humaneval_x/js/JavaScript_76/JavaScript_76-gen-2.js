  let result = 1;
  let i = 0;
  while (result < x) {
    result *= n;
    i += 1;
  }
  return result == x && i == Math.log(x) / Math.log(n);
}



