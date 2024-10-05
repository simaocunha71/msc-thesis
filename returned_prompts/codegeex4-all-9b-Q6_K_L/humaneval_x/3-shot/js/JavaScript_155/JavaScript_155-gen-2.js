  var numStr = Math.abs(num).toString();
  var evenCount = 0;
  var oddCount = 0;

  for (var i = 0; i < numStr.length; i++) {
    if (numStr[i] % 2 == 0) {
      evenCount += 1;
    } else {
      oddCount += 1;
    }
  }

  return [evenCount, oddCount];
}