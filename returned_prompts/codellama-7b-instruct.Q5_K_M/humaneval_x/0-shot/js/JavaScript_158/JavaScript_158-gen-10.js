const findMax = (words) => {
  words.sort((a, b) => {
    const aCount = new Set(a).size;
    const bCount = new Set(b).size;
    if (aCount === bCount) {
      return a.localeCompare(b);
    }
    return bCount - aCount;
  });
  return words[0];
}
