  let count = new Map();
  for (const i of lst) {
    if (count.has(i)) {
      count.set(i, count.get(i) + 1);
    } else {
      count.set(i, 1);
    }
  }

  let result = -1;
  for (const i of lst) {
    if (i > count.get(i)) {
      continue;
    } else if (result < i) {
      result = i;
    }
  }
  return result;
}



