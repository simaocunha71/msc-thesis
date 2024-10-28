  return Math.max(...l);
}
// OR
const maxElement = (l) => {
  return Math.max.apply(null, l);
}
// OR
const maxElement = (l) => {
  let max = l[0];
  for (let i = 1; i < l.length; i++) {
    if (l[i] > max) {
      max = l[i];
    }
  }
  return max;
}