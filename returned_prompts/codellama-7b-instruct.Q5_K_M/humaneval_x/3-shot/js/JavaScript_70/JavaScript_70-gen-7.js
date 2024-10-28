  if (lst.length == 0) {
    return [];
  }

  let result = [];
  let min_idx = 0;
  let max_idx = 0;

  for (let i = 0; i < lst.length; i++) {
    if (lst[min_idx] > lst[i]) {
      min_idx = i;
    }
    if (lst[max_idx] < lst[i]) {
      max_idx = i;
    }
  }

  result.push(lst[min_idx]);
  result.push(lst[max_idx]);
  result.push(lst[min_idx]);

  return result;
}



