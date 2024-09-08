  let result = {
    'even': 0,
    'odd': 0
  };
  for (let i = 1; i <= n; i++) {
    let s = i.toString();
    if (s === s.split('').reverse().join('')) {
      if (i % 2 == 0) {
        result.even += 1;
      } else {
        result.odd += 1;
      }
    }
  }
  return [result.even, result.odd];
}



