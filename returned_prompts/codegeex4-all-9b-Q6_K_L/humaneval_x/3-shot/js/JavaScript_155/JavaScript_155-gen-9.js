  var numString = Math.abs(num).toString();
  var numArray = numString.split('');
  var evenCount = 0;
  var oddCount = 0;
  for (var i = 0; i < numArray.length; i++) {
    if (parseInt(numArray[i]) % 2 == 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }
  return [evenCount, oddCount];
}



