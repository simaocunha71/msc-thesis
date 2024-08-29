  if (lst.length == 0 || lst.every(x => x >= 0)) {
    return [null, null];
  }

  let min = Math.min(...lst);
  let max = Math.max(...lst);

  if (min < 0 && max > 0) {
    return [max, min];
  } else {
    return [null, null];
  }
}



