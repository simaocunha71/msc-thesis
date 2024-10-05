  if (x > y) {
    return -1;
  }
  let min = Math.floor(x / 2) * 2;
  let max = Math.ceil(y / 2) * 2;
  if (min > y) {
    return -1;
  } else {
    return min;
  }
}