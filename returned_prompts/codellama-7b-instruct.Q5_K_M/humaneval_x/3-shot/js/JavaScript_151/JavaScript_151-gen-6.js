  let result = 0;
  let sum = 0;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] % 1 == 0 && lst[i] > 0) {
      sum += lst[i];
    }
  }

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] % 1 == 0 && lst[i] > 0 && lst[i] % 2 != 0) {
      result += lst[i] ** 2;
    }
  }

  return result;
}



