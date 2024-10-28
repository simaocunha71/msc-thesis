  var result = [];
  var count = 0;
  for (var i = 0; i < lst.length; i++) {
    for (var j = 0; j < lst[i].length; j++) {
      if (lst[i][j] == x) {
        result.push([i, j]);
        count++;
      }
    }
  }
  result.sort((a, b) => {
    if (a[0] < b[0]) return -1;
    else if (a[0] > b[0]) return 1;
    else {
      if (a[1] < b[1]) return 1;
      else if (a[1] > b[1]) return -1;
      else return 0;
    }
  });
  return result;
}



