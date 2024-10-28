  if (lst.length < 2) {
    return true;
  }

  if (lst.length == 2) {
    return lst[0] < lst[1];
  }

  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] > lst[i + 1]) {
      return false;
    }
  }

  return true;
}



