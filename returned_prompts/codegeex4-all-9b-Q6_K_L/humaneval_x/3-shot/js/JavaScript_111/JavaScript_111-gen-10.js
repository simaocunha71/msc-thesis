  var result = {};

  var list = test.split(' ');
  for (var i = 0; i < list.length; i++) {
    var count = 0;
    for (var j = 0; j < list.length; j++) {
      if (list[i] == list[j]) {
        count += 1;
      }
    }
    if (result[list[i]] == undefined) {
      result[list[i]] = count;
    } else if (count > result[list[i]]) {
      result[list[i]] = count;
    }
  }

  return result;
}



