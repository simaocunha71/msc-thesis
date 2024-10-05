const isBored = (S) => {
  let count = 0;
  for (let i = 0; i < S.length; i++) {
    if (S[i] === 'I') {
      count++;
    }
  }
  return count;
};
