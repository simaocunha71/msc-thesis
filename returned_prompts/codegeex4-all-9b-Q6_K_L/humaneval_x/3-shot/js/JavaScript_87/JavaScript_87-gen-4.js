  var result = [];
  for (var i = 0; i < lst.length; i++) {
    for (var j = 0; j < lst[i].length; j++) {
      if (lst[i][j] == x) {
        result.push([i, j]);
      }
    }
  }
  return result;
}



