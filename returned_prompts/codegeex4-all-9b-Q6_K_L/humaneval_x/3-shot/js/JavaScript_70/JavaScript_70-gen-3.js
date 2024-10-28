  var result = [];
  var lst_copy = [...lst];

  while (lst_copy.length > 0) {
    result.push(Math.min(...lst_copy));
    lst_copy.splice(lst_copy.indexOf(Math.min(...lst_copy)), 1);
    if (lst_copy.length > 0) {
      result.push(Math.max(...lst_copy));
      lst_copy.splice(lst_copy.indexOf(Math.max(...lst_copy)), 1);
    }
  }

  return result;
}



