  let result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(...l.slice(i, i + 1).sort());
    } else {
      result.push(l[i]);
    }
  }
  return result;
}...



