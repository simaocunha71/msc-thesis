  let countEven = 0, countOdd = 0;
  for (let i = 1; i < n; i++) {
    let str = i.toString();
    if (str === str.split('').reverse().join('')) {
      if (i % 2 === 0) {
        countEven++;
      } else {
        countOdd++;
      }
    }
  }
  return [countEven, countOdd];
}



