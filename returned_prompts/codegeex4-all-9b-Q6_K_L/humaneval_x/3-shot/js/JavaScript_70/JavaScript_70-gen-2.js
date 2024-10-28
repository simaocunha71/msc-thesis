  var result = [];
  var i = 0;
  while (lst.length > 0) {
    if (i % 2 == 0) {
      result.push(Math.min(...lst));
    } else {
      result.push(Math.max(...lst));
    }
    lst.splice(lst.indexOf(Math.min(...lst)), 1);
  }
  return result;
}

