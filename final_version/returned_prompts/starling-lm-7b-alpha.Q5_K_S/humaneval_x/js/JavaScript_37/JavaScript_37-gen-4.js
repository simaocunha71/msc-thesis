  let result = [];

  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(l[i]);
    } else {
      result.push(l[i]);
    }
  }

  result[1] = result.sort((a, b) => a - b)[1];

  return result;
}



