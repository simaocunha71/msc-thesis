  let result = [];
  let current = n;

  while (current != 1) {
    if (current % 2 != 0) {
      result.push(current);
    }
    if (current % 2 == 0) {
      current = current / 2;
    } else {
      current = 3 * current + 1;
    }
  }

  return result;
}



