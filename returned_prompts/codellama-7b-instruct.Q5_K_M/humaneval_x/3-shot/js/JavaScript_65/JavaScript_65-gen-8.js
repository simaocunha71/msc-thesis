  var str = x.toString();
  var len = str.length;

  if (shift > len) {
    return str.split('').reverse().join('');
  }

  var result = '';
  for (var i = 0; i < len; i++) {
    var index = (i + shift) % len;
    result += str[index];
  }

  return result;
}



