const countUpper = (s) => {
  return s.split('').filter((s, i) => i % 2 === 0 && s === s.toUpperCase()).length;
};

B:
const countUpper = (s) => {
  return s.split('').filter((s, i) => i % 2 === 0 && s === s.toUpperCase()).length;
};

C:
const countUpper = s => {
  return s.split('').filter((s, i) => i % 2 === 0 && s === s.toUpperCase()).length;
};
