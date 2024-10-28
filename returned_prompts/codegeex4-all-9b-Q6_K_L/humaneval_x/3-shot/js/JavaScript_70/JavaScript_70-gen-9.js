  var result = [];
  var current_min = 0;
  var current_max = 0;

  if (lst.length == 0) {
    return result;
  }

  while (lst.length > 0) {
    if (current_min == 0) {
      result.push(Math.min(...lst));
      current_min = 1;
      current_max = 0;
    } else {
      result.push(Math.max(...lst));
      current_min = 0;
      current_max = 1;
    }
    lst.splice(lst.indexOf(Math.max(...lst)), 1);
  }

  return result;
}