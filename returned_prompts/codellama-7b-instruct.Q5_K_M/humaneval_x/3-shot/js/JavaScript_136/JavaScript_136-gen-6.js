  let negative_int = null;
  let positive_int = null;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0) {
      if (negative_int == null || lst[i] > negative_int) {
        negative_int = lst[i];
      }
    }
    if (lst[i] > 0) {
      if (positive_int == null || lst[i] < positive_int) {
        positive_int = lst[i];
      }
    }
  }

  return [negative_int, positive_int];
}



