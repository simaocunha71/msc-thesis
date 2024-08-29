  let result = [0, 0];
  for (let i = 1; i <= n; i++) {
    let s = i.toString();
    if (s === s.split('').reverse().join('')) {
      result[i % 2] += 1;
    }
  }
  return result;
}



