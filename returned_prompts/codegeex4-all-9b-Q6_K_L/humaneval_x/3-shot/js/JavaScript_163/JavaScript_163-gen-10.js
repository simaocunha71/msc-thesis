  var result = [];

  for (var i = a; i <= b; i++) {
    var str = i.toString();
    for (var j = 0; j < str.length; j++) {
      if (str[j] % 2 == 0) {
        result.push(parseInt(str[j]));
      }
    }
  }

  return result;
}



