  let max_negative = null;
  let min_positive = null;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0) {
      if (max_negative === null || lst[i] > max_negative) {
        max_negative = lst[i];
      }
    } else if (lst[i] > 0) {
      if (min_positive === null || lst[i] < min_positive) {
        min_positive = lst[i];
      }
    }
  }

  return [max_negative === null ? null : max_negative, min_positive === null ? null : min_positive];
}