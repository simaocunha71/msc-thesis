  let result = 0;
  let i = 0;
  while (i < lst.length) {
    if (lst[i] % 2 == 0 && i % 2 != 0) {
      result += lst[i];
    }
    i += 1;
  }
  return result;
}



