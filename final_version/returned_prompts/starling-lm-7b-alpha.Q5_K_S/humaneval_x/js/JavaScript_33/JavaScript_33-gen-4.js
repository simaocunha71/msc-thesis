  let result = [];

  for (let i = 0; i < l.length; i++) {
    if (i % 3 == 0) {
      result.push(l[i]);
    } else {
      result.push(l[i]);
    }
  }

  result[result.length - 1] = result[result.length - 1].sort();

  return result;
}



