  let min = Infinity;
  let secMin = Infinity;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < min) {
      secMin = min;
      min = lst[i];
    } else if (lst[i] < secMin && lst[i] !== min) {
      secMin = lst[i];
    }
  }
  return secMin === Infinity ? null : secMin;
}