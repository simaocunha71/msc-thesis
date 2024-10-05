  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] > 0 && lst[i] % 2 !== 0 && Number.isInteger(lst[i])) {
      sum += lst[i] ** 2;
    }
  }
  return sum;
}



