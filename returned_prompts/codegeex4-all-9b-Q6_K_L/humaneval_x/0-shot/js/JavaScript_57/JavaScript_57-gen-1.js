const monotonic = (l) => {
  if (l.length < 2) return true;
  const direction = l[0] - l[1] > 0 ? -1 : 1;
  for (let i = 1; i < l.length - 1; i++) {
    if ((l[i] - l[i + 1]) * direction <= 0) return false;
  }
  return true;
}