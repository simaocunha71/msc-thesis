  if (lst.length < 2) {
    return null;
  }
  let min = lst[0];
  let secondMin = null;
  for (let num of lst) {
    if (num < min) {
      secondMin = min;
      min = num;
    } else if (num < secondMin) {
      secondMin = num;
    }
  }
  return secondMin === null ? null : secondMin;
}