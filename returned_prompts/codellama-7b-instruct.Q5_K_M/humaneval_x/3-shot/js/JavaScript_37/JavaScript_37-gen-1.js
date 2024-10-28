  const result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(l[i]);
    } else {
      result.push(l[i].sort((a, b) => a - b));
    }
  }
  return result;
}



