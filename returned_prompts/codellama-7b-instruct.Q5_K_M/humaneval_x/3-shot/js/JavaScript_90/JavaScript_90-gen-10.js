  if (lst.length < 2) return null;

  let min = lst[0];
  let min_index = 0;

  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < min) {
      min = lst[i];
      min_index = i;
    }
  }

  return lst[min_index + 1];
}



