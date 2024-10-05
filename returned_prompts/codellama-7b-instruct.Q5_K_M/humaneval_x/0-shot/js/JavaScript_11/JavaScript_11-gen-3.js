const stringXor = (a, b) => {
  return a.split('').map((x, i) => +(x ^ b[i])).join('');
};

B:
const stringXor = (a, b) => {
  return a.split('').map((x, i) => x ^ b[i]).join('');
};

C:
const stringXor = (a, b) => a.split('').map((x, i) => x ^ b[i]).join('');

D:
const stringXor = (a, b) => a.split('').map((x, i) => +(x ^ b[i])).join('');
