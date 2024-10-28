  if (lst.length <= 1) {
    return lst;
  }

  lst.sort((a, b) => a - b);
  let result = [];
  let min = lst.shift();
  result.push(min);

  while (lst.length > 0) {
    let max = Math.max(...lst);
    result.push(max);
    lst.splice(lst.indexOf(max), 1);
    if (lst.length > 0) {
      let min = Math.min(...lst);
      result.push(min);
      lst.splice(lst.indexOf(min), 1);
    }
  }

  return result;
}