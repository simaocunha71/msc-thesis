  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      if (l[i] + l[j] === 0) {
        return true;
      }
    }
  }
  return false;
}
// or using Set
const pairsSumToZero = (l) => {
  const seen = new Set();
  for (let num of l) {
    if (seen.has(-num)) {
      return true;
    }
    seen.add(num);
  }
  return false;
}