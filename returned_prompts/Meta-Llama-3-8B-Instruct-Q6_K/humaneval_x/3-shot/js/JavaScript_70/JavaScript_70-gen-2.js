  if (lst.length == 0) {
    return lst;
  }
  let sorted = lst.slice().sort((a, b) => a - b);
  let result = [];
  while (sorted.length > 0) {
    result.push(sorted.shift());
    if (sorted.length > 0) {
      sorted = sorted.sort((a, b) => b - a).slice(1);
    }
  }
  return result;
}