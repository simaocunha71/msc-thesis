  let even = 0;
  let odd = 0;
  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    if (str === str.split('').reverse().join('')) {
      if (i % 2 === 0) {
        even += 1;
      } else {
        odd += 1;
      }
    }
  }
  return [even, odd];
}


