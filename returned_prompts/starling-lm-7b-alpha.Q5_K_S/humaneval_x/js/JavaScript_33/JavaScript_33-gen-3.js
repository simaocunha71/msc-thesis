  let result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 3 === 0) {
      result.push(l.sort((a, b) => a - b)[i]);
    } else {
      result.push(l[i]);
    }
  }
  return result;
}



