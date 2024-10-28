  var result = [];

  if (lst.length == 0) {
    return result;
  }

  for (var i = 0; i < lst.length; i++) {
    var row = lst[i];
    for (var j = 0; j < row.length; j++) {
      if (row[j] == x) {
        result.push([i, j]);
      }
    }
  }

  result.sort(function (a, b) {
    if (a[1] < b[1]) {
      return 1;
    } else if (a[1] > b[1]) {
      return -1;
    } else {
      return 0;
    }
  });

  result.sort(function (a, b) {
    if (a[0] < b[0]) {
      return -1;
    } else if (a[0] > b[0]) {
      return 1;
    } else {
      return 0;
    }
  });

  return result;
}



