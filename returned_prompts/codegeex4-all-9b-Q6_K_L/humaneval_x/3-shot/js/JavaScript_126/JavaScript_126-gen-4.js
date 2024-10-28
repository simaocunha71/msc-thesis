  for (let i = 0; i < lst.length; i++) {
    for (let j = i + 1; j < lst.length; j++) {
      if (lst[i] > lst[j]) {
        return false;
      }
    }
  }
  return true;
}

