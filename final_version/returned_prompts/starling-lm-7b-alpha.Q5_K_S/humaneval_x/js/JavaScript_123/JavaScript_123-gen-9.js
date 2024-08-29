  let result = [];
  let cur = n;

  while (cur != 1) {
    if (cur % 2) {
      result.push(cur);
      cur = 3 * cur + 1;
    } else {
      cur = cur / 2;
    }
  }

  return result.sort((a, b) => a - b);
}



