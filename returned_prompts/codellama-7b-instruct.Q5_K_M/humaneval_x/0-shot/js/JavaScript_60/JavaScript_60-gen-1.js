
const sumToN = (n) => {
  let sum = 0;
  for (let i = 1; i <= n; i++) sum += i;
  return sum;
};

B:

const sumToN = (n) => (n * (n + 1)) / 2;

C:

const sumToN = n => n > 1 ? n + sumToN(n - 1) : n;

D:

const sumToN = n => n < 1 ? 0 : n + sumToN(n - 1);

E:

const sumToN = n => n < 1 ? 0 : n + (n - 1) * n / 2;

F:

const sumToN = n => n < 1 ? 0 : n + (n - 1) * (n + 1) / 2;

G:

const sumToN = n => n < 1 ? 0 : n + (n - 1) * (n + 1) / 2;

H:

const sumToN = n => n < 1 ? 0 : n + (n - 1) * (n + 1) / 2;

I:

const sumToN = n => n < 1 ? 0 : n + (n - 1) * (n + 1) / 2;

J:

const sumToN = n => n < 1 ? 0 : n + (n - 1) * (n + 1) / 2;

K:

const sumToN = n => n < 1 ? 0 : n + (n - 1) * (n + 1) / 2;

L:

const sumToN = n => n < 1 ? 0 : n + (n - 1) * (n + 1) / 2;

M:

const sumToN = n => n < 1 ? 0 : n + (n - 1) * (n + 1) / 2;

N:

const sumToN = n => n < 1 ? 