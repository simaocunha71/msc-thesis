  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] >= lst[i + 1]) {
      if (lst.filter(x => x === lst[i]).length > 1) {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
}