/*
  >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
  [0, 2, 3, 5, 9, 123]
  */
const unique = (l) => {
  const unique = [...new Set(l)];
  return unique.sort();
}

