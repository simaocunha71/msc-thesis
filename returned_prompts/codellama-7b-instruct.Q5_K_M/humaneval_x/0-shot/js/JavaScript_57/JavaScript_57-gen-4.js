  const diffs = [];
  for (let i = 1; i < l.length; i++) {
    diffs.push(l[i] - l[i - 1]);
  }
  return diffs.every((e, i, a) => e == a[i - 1]);
}