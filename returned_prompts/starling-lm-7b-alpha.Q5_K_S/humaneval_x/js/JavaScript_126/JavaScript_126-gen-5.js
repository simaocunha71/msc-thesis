  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i + 1] < lst[i]) {
      return false;
    }
  }
  return true;
}



