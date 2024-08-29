  let result = [];
  l1.sort();
  l2.sort();
  let i = 0;
  let j = 0;

  while (i < l1.length && j < l2.length) {
    if (l1[i] == l2[j]) {
      result.push(l1[i]);
      i += 1;
      j += 1;
    } else if (l1[i] < l2[j]) {
      i += 1;
    } else {
      j += 1;
    }
  }

  return result;
}



