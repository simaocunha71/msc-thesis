  let negative = null;
  let positive = null;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0) {
      if (negative === null || lst[i] > negative) {
        negative = lst[i];
      }
    } else if (lst[i] > 0) {
      if (positive === null || lst[i] < positive) {
        positive = lst[i];
      }
    }
  }
  return [negative, positive];
}