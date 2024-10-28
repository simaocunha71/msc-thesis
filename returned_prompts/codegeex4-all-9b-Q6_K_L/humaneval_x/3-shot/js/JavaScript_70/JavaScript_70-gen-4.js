  var result = [];
  if (lst.length == 0) {
    return result;
  }

  var current = 0;
  while (lst.length > 0) {
    if (current == 0) {
      result.push(Math.min(...lst));
      lst.splice(lst.indexOf(Math.min(...lst)), 1);
    } else {
      result.push(Math.max(...lst));
      lst.splice(lst.indexOf(Math.max(...lst)), 1);
    }
    current = 1 - current;
  }
  return result;
}



