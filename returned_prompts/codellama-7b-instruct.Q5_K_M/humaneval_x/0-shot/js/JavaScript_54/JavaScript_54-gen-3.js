const sameChars = (s0, s1) => {
  const s0Arr = s0.split('');
  const s1Arr = s1.split('');
  return s0Arr.every(char => s1Arr.includes(char));
};
