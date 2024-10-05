  var result = [];
  var count = 0;

  for (var i = 0; i < lst.length; i++) {
    for (var j = 0; j < lst[i].length; j++) {
      if (parseInt(lst[i][j]) % 2 != 0) {
        count += 1;
      }
    }
    result.push(count);
    count = 0;
  }

  return result;
}



