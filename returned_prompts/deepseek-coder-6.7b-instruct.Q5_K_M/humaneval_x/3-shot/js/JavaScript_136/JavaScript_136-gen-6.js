  let negMax = null;
  let posMin = null;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (negMax === null || lst[i] > negMax)) {
      negMax = lst[i];
    } else if (lst[i] > 0 && (posMin === null || lst[i] < posMin)) {
      posMin = lst[i];
    }
  }
  return [negMax, posMin];
}



