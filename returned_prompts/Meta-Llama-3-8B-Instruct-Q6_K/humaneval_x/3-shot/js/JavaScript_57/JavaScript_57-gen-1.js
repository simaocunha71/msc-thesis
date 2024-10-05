  for (let i = 1; i < l.length; i++) {
    if (l[i] > l[i - 1]) {
      for (let j = i + 1; j < l.length; j++) {
        if (l[j] < l[j - 1]) {
          return false;
        }
      }
      return true;
    } else if (l[i] < l[i - 1]) {
      for (let j = i + 1; j < l.length; j++) {
        if (l[j] > l[j - 1]) {
          return false;
        }
      }
      return true;
    }
  }
  return true;
}
// Example of a more concise solution:
const monotonic = l => l.every((x, i, a) => (i == 0 || x >= a[i - 1]) && (i == a.length - 1 || x <= a[i + 1]));