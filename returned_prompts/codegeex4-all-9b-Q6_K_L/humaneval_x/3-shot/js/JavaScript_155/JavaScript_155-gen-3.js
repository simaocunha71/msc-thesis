  var numString = Math.abs(num).toString();
  var evenCount = 0;
  var oddCount = 0;
  for (const c of numString) {
    if (parseInt(c) % 2 == 0) {
      evenCount += 1;
    } else {
      oddCount += 1;
    }
  }
  return [evenCount, oddCount];
}



