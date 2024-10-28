  let evenCount = 0;
  let oddCount = 0;
  let absNum = Math.abs(num);
  while (absNum > 0) {
    let digit = absNum % 10;
    if (digit % 2 === 0) {
      evenCount += 1;
    } else {
      oddCount += 1;
    }
    absNum = Math.floor(absNum / 10);
  }
  return [evenCount, oddCount];
}



