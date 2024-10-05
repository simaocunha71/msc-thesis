  var sum = 0;
  for (var i = 0; i < s.length; i++) {
    var code = s.charCodeAt(i);
    if (code >= 65 && code <= 90) {
      sum += code;
    }
  }
  return sum;
}



