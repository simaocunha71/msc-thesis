  var numStr = x.toString();
  shift = shift % numStr.length;
  return numStr.substring(shift) + numStr.substring(0, shift);
}