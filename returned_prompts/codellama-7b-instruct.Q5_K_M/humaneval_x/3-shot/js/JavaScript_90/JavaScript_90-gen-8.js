  if (lst.length < 2) {
    return null;
  }

  var min_idx = 0;
  var min_val = lst[0];
  for (var i = 1; i < lst.length; i++) {
    if (lst[i] < min_val) {
      min_idx = i;
      min_val = lst[i];
    }
  }

  return lst[min_idx + 1];
}



