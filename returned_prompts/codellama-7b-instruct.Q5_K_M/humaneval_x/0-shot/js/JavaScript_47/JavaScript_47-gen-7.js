const median = (l) => {
  let sorted = l.sort();
  if (l.length % 2 == 0) {
    return (sorted[l.length/2] + sorted[l.length/2 - 1]) / 2;
  } else {
    return sorted[Math.floor(l.length/2)];
  }
};
