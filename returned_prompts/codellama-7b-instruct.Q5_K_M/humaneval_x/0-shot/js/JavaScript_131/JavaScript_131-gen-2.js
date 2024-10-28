const digits = (n) => {
  const arr = n.toString().split('');
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 1) {
      result.push(arr[i]);
    }
  }
  return result.join('');
};

B:
const digits = (n) => {
  let result = 1;
  for (let i = 0; i < n.length; i++) {
    if (n[i] % 2 !== 0) {
      result *= n[i];
    }
  }
  return result;
};

C:
const digits = (n) => {
  return n.toString().split('').reduce((a, b) => parseInt(b) % 2 === 1 ? a * b : a, 1);
};

D:
const digits = (n) => {
  return n.toString().split('').filter(i => i % 2 === 1).join('');
};

E:
const digits = (n) => {
  return n.toString().split('').reduce((a, b) => a * b, 1);
};

F:
const digits = (n) => {
  return n.toString().split('').reduce((a, b) => a * b, 1);
};

G:
const digits = (n) => {
  return n.toString().split('').filter(i => i % 2 === 1).join('');
};

H:
const digits = (n) => {
  return n.toString().split('').reduce((a, b) => parseInt(b) % 2 === 1 ? a * b : a, 1);
};

I:
const digits = (n) => {
  return n.toString().split('').reduce((a, b) => a * b, 1);
};

J:
const digits = (n) => {
  return n.toString().split('').filter(i => i % 2 === 1).join('');
};

K: