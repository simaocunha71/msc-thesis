  const result = [0, 0];

  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    if (str === str.split('').reverse().join('')) {
      if (i % 2 == 0) {
        result[0] += 1;
      } else {
        result[1] += 1;
      }
    }
  }

  return result;
}



