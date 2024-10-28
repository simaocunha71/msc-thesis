  let result = [];
  let current = n;

  while (current != 1) {
    if (current % 2 == 0) {
      current = Math.floor(current / 2);
    } else {
      current = 3 * current + 1;
    }
    result.push(current);
  }
  return result;
}



