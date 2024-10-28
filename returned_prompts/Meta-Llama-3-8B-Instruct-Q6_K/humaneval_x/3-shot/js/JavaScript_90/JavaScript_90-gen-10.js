  if (lst.length < 2) return null;
  let min = Infinity;
  let secondMin = Infinity;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < min) {
      secondMin = min;
      min = lst[i];
    } else if (lst[i] < secondMin && lst[i] !== min) {
      secondMin = lst[i];
    }
  }
  return secondMin === Infinity ? null : secondMin;
}