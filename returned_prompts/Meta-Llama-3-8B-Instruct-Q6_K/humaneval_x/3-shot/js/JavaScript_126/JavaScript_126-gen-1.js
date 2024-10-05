  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] >= lst[i + 1]) {
      if (lst.indexOf(lst[i]) != lst.indexOf(lst[i + 1])) {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
}