  let counter = 1;
  while (counter < lst.length) {
    if (lst[counter] <= lst[counter - 1]) {
      return false;
    }
    counter += 1;
  }
  return true;
}



