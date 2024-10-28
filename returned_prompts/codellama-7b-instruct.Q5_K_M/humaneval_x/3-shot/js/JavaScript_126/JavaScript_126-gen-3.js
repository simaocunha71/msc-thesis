  if (lst.length == 1) {
    return true;
  }

  if (lst.length == 2) {
    if (lst[0] == lst[1]) {
      return false;
    }
    return lst[0] < lst[1];
  }

  for (let i = 1; i < lst.length; i++) {
    if (lst[i] == lst[i-1]) {
      return false;
    }
    if (lst[i] < lst[i-1]) {
      return false;
    }
  }
  return true;
}



