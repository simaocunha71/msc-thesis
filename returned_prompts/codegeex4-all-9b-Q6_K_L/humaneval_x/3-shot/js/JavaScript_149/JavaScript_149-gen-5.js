  var result = [];

  for (var i = 0; i < lst.length; i++) {
    if (lst[i].length % 2 == 0) {
      result.push(lst[i]);
    }
  }

  result.sort(function (a, b) {
    if (a.length == b.length) {
      return a.localeCompare(b);
    } else {
      return a.length - b.length;
    }
  });

  return result;
}



