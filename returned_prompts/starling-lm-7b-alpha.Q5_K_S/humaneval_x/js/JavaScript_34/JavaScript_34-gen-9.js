  let result = [];
  for (let i = 0; i < l.length; i++) {
    if (result.indexOf(l[i]) == -1) {
      result.push(l[i]);
    }
  }
  result.sort((a, b) => a - b);
  return result;
}


