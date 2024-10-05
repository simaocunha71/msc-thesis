  var sum = 0;
  for (var i = 0; i < s.length; i++) {
    var charCode = s.charCodeAt(i);
    if (charCode >= 65 && charCode <= 90) {
      sum += charCode;
    }
  }
  return sum;
}



