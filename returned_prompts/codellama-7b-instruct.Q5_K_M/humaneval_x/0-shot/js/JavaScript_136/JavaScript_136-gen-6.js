  let neg = [];
  let pos = [];

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0) {
      neg.push(lst[i]);
    } else if (lst[i] > 0) {
      pos.push(lst[i]);
    }
  }

  let a = Math.max(...neg);
  let b = Math.min(...pos);

  return [a, b];
}
