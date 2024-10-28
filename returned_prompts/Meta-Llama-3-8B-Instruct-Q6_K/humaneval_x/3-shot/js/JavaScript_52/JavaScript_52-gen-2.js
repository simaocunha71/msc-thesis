  for (let i = 0; i < l.length; i++) {
    if (l[i] >= t) {
      return false;
    }
  }
  return true;
}
// or
const belowThreshold = (l, t) => l.every(x => x < t);
// or
const belowThreshold = (l, t) => l.reduce((a, b) => a && b < t, true);
// or
const belowThreshold = (l, t) => !l.some(x => x >= t);
// or
const belowThreshold = (l, t) => l.every(x => x < t);
// or
const belowThreshold = (l, t) => l.filter(x => x >= t).length === 0;