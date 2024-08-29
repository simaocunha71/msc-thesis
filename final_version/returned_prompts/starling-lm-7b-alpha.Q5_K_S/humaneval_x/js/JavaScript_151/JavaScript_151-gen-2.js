  let result = 0;
  for (let i = 0; i < lst.length; i++) {
    if (typeof lst[i] === 'number' && lst[i] >= 0 && lst[i] % 1 === 0) {
      if (lst[i] % 2 === 1) {
        result += lst[i] ** 2;
      }
    }
  }
  return result;
}



