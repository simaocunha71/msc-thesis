  let evenCount = 0;
  let oddCount = 0;

  for (let digit of num.toString().split('')) {
    let n = parseInt(digit);
    if (n % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }

  return [evenCount, oddCount];
}