  let last = lst[0];
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < last) {
      return false;
    }
    if (lst[i] == last) {
      return false;
    }
    last = lst[i];
  }
  return true;
}



