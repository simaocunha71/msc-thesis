const maxElement = (l) => {
  let max = -Infinity;
  for (let i = 0; i < l.length; i++) {
    if (l[i] > max) max = l[i];
  }
  return max;
};

B:
const maxElement = (l) => {
  let max = l[0];
  for (let i = 1; i < l.length; i++) {
    if (l[i] > max) max = l[i];
  }
  return max;
};

C:
const maxElement = (l) => {
  let max = l.reduce((a, b) => Math.max(a, b));
  return max;
};

D:
const maxElement = (l) => {
  l.sort((a, b) => b - a);
  return l[0];
};
