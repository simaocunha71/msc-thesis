  var result = [];

  for (var i = 0; i < lst.length; i++) {
    if (lst[i].length % 2 == 0) {
      result.push(lst[i]);
    }
  }

  return result.sort();
}