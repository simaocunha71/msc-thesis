  let result = 0;
  let index = 0;
  while (index < lst.length) {
    if (lst[index] % 2 == 0 && index % 2 != 0) {
      result += lst[index];
    }
    index += 1;
  }
  return result;
}



