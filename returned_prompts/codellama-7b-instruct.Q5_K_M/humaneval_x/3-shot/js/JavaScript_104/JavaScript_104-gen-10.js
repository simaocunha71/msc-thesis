  var result = [];
  var unique = [];
  for (var i = 0; i < x.length; i++) {
    var temp = x[i].toString();
    for (var j = 0; j < temp.length; j++) {
      if (temp[j] % 2 != 0) {
        unique.push(temp[j]);
      }
    }
    if (unique.length > 0) {
      result.push(parseInt(unique.join('')));
    }
    unique = [];
  }

  return result.sort((a, b) => a - b);
}



