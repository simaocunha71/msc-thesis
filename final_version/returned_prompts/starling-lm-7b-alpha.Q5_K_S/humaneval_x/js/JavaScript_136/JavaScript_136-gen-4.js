  let negative = -Infinity;
  let positive = Infinity;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && lst[i] > negative) {
      negative = lst[i];
    }
    if (lst[i] > 0 && lst[i] < positive) {
      positive = lst[i];
    }
  }

  if (negative === -Infinity && positive === Infinity) {
    return [null, null];
  }

  return [negative, positive];
}



