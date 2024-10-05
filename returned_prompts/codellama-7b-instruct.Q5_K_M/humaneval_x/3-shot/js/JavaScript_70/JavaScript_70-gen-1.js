  let result = [];

  if (lst.length == 0) {
    return result;
  }

  let min_value = Math.min(...lst);
  let max_value = Math.max(...lst);

  while (lst.includes(min_value)) {
    result.push(min_value);
    lst.splice(lst.indexOf(min_value), 1);
    if (lst.length == 0) {
      break;
    }
    min_value = Math.min(...lst);
    max_value = Math.max(...lst);
  }

  result.push(max_value);

  while (lst.includes(min_value)) {
    result.push(min_value);
    lst.splice(lst.indexOf(min_value), 1);
    if (lst.length == 0) {
      break;
    }
    min_value = Math.min(...lst);
    max_value = Math.max(...lst);
  }

  return result;
}



