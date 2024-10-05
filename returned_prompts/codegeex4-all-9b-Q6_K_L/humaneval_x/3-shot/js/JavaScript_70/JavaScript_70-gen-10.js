  var result = [];
  var odd = true;

  while (lst.length > 0) {
    if (odd) {
      var min = Math.min(...lst);
      var index = lst.indexOf(min);
      result.push(min);
      lst.splice(index, 1);
    } else {
      var max = Math.max(...lst);
      var index = lst.indexOf(max);
      result.push(max);
      lst.splice(index, 1);
    }
    odd = !odd;
  }

  return result;
}



