  const isPrime = (n) => {
    if (n < 2) return false;
    for (let i = 2; i < n; i++) if (n % i === 0) return false;
    return true;
  };

B:
  const xOrY = (n, x, y) => {
    if (isPrime(n)) return x;
    else return y;
  };
};

const xOrY = (n, x, y) => {

C:
  if (n % 2 === 0) return y;

D:
  return x;
};

E:
const isPrime = (n) => {
  if (n < 2) return false;
  for (let i = 2; i < n; i++) if (n % i === 0) return false;
  return true;
};

F:
const xOrY = (n, x, y) => {
  if (isPrime(n)) return x;
  else return y;
};

G:
const xOrY = (n, x, y) => {
  if (n % 2 === 0) return y;
  return x;
};

H:
const xOrY = (n, x, y) => {
  if (isPrime(n)) return x;
  else return y;
};

I:
const xOrY = (n, x, y) => {
  if (n % 2 === 0) return y;
  return x;
};

J:
const xOrY = (n, x, y) => {
  if (isPrime(n)) return x;
  else return y;
};

K:
const xOrY = (n, x, y) => {
  if (n % 2 === 0) return y;
  return x;
};

L:
const xOrY = (n, x, y) => {
  if (isPrime(n)) return x;
  else return y;
};

M:
const xOrY = (n, x, y) =>