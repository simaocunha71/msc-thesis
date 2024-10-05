  var str = x.toString();
  var len = str.length;
  if (shift > len) {
    return str.split("").reverse().join("");
  }

  var newStr = str.slice(len - shift, len) + str.slice(0, len - shift);
  return newStr;
}



