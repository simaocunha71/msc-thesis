  var result = [];
  while (lst.length > 0) {
    result.push(Math.min(...lst));
    lst.splice(lst.indexOf(Math.min(...lst)), 1);
    if (lst.length > 0) {
      result.push(Math.max(...lst));
      lst.splice(lst.indexOf(Math.max(...lst)), 1);
    }
  }
  return result;
}