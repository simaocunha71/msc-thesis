  var sum = 0;
  for (var i = 0; i < s.length; i++) {
    var c = s.charAt(i);
    var code = c.charCodeAt(0);
    if (code >= 65 && code <= 90) {
      sum += code;
    }
  }
  return sum;
}



