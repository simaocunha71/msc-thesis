  var binaryString = N.toString(2);
  var binarySum = 0;
  for (var i = 0; i < binaryString.length; i++) {
    binarySum += parseInt(binaryString[i]);
  }
  return binarySum.toString();
}



