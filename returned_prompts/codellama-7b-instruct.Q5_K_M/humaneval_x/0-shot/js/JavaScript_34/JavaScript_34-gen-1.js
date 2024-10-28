/*Return sorted unique elements in a list
  >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
  [0, 2, 3, 5, 9, 123]
  */
const unique = (l) => {
  const seen = new Set();
  const result = [];

  for (let i = 0; i < l.length; i++) {
    const item = l[i];
    if (!seen.has(item)) {
      seen.add(item);
      result.push(item);
    }
  }
  return result.sort((a, b) => a - b);
}

