  let result = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] % 1 === 0 && lst[i] >= 0 && lst[i] % 2 === 1) {
      result += Math.pow(lst[i], 2);
    }
  }
  return result;
}


