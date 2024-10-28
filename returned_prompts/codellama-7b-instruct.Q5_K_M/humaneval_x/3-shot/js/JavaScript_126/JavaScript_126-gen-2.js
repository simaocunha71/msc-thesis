  if (lst.length == 1) {
    return true;
  } else if (lst.length == 0) {
    return false;
  } else {
    for (let i = 1; i < lst.length; i++) {
      if (lst[i] < lst[i - 1]) {
        return false;
      }
    }
    return true;
  }
}



