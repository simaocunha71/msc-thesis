  let previous = lst[0];

  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < previous) {
      return false;
    }
    previous = lst[i];
  }

  return true;
}



