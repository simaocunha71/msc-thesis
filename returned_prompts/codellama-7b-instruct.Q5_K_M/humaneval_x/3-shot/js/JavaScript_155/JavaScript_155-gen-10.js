  var evenCount = 0;
  var oddCount = 0;
  var temp = num;

  while (temp > 0) {
    if (temp % 10 % 2 == 0) {
      evenCount++;
    } else {
      oddCount++;
    }
    temp = Math.floor(temp / 10);
  }

  return [evenCount, oddCount];
}



