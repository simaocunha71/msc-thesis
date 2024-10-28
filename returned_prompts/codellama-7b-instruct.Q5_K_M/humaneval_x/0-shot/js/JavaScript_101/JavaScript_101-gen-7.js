const wordsString = (s) => {
  return s.split(/\W+/);
};

B:
const wordsString = (s) => {
  return s.split(/\s*,\s*|\s+/);
};

C:
const wordsString = (s) => {
  return s.match(/\w+/g);
};

D:
const wordsString = (s) => {
  return s.trim().split(/\s*,\s*|\s+/);
};

E:
const wordsString = (s) => {
  return s.trim().split(/\W+/);
};
