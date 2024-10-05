  var result = [];
  for (var i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(l[i]);
    } else {
      var temp = l[i];
      temp.sort();
      result.push(temp);
    }
  }
  return result;
}



