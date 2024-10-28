  if (lst.length == 1) {
    return true;
  }
  if (lst.length == 0) {
    return false;
  }
  if (lst.length > 1) {
    for (let i = 0; i < lst.length - 1; i++) {
      if (lst[i] > lst[i + 1]) {
        return false;
      }
    }
    return true;
  }
}



