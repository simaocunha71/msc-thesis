  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < lst[i - 1]) {
      return false;
    }
  }
  return true;
}

//isSorted([1, 2, 3, 4, 5, 6, 7])

