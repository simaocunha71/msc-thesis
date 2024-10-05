const pairsSumToZero = (l) => {
  const set = new Set();
  for (let i = 0; i < l.length; i++) {
    if (set.has(-l[i])) {
      return true;
    }
    set.add(l[i]);
  }
  return false;
};

