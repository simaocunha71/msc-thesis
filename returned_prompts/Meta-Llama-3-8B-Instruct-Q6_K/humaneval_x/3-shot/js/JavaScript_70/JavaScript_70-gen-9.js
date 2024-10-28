  if (lst.length === 0) {
    return [];
  }
  lst.sort((a, b) => a - b);
  let result = [lst[0]];
  let min = lst[0];
  let max = lst[0];
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < min) {
      min = lst[i];
      result.push(min);
    } else if (lst[i] > max) {
      max = lst[i];
      result.push(max);
    }
  }
  return result;
}