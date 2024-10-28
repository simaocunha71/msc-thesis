  var str = x.toString();
  var len = str.length;
  var newStr = str.substring(len - shift) + str.substring(0, len - shift);
  return newStr;
}