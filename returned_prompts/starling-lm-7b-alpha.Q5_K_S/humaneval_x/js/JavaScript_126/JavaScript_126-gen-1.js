  let prev = lst[0];
  for (let i = 1; i < lst.length; i++) {
    if (prev < lst[i]) {
      prev = lst[i];
    } else {
      return false;
    }
  }

  return true;
}



