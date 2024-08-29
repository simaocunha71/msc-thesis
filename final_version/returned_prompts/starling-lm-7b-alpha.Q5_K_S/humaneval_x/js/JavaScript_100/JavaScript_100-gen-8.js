  let result = [];
  let current = n;

  while (current > 0) {
    result.push(current);
    if (current % 2 == 0) {
      current += 2;
    } else {
      current += 1;
    }
  }

  return result;
}



