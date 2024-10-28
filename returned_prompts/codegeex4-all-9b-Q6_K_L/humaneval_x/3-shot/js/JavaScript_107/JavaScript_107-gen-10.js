  var evenCount = 0;
  var oddCount = 0;
  for (let i = 1; i <= n; i++) {
    let s = i.toString();
    if (s == s.split('').reverse().join('')) {
      if (i % 2 == 0) {
        evenCount += 1;
      } else {
        oddCount += 1;
      }
    }
  }
  return [evenCount, oddCount];
}



