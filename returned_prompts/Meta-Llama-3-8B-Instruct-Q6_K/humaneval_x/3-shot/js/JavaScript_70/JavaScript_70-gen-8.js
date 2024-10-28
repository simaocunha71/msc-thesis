  if (lst.length == 0) {
    return [];
  }
  let result = [];
  let sorted = lst.slice().sort((a, b) => a - b);
  let min = sorted.shift();
  result.push(min);
  while (sorted.length > 0) {
    let max = sorted.reduce((max, current) => current > max ? current : max);
    result.push(max);
    sorted.splice(sorted.indexOf(max), 1);
  }
  return result;
}