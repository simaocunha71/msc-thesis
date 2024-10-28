const largestPrimeFactor = (n) => {
  let i = 2;
  while (i <= Math.sqrt(n)) {
    if (n % i === 0) {
      n = n / i;
      i = 2;
    } else {
      i++;
    }
  }
  return n;
};

// 41ms
const largestPrimeFactor = n => {
  if (n === 1) return;
  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      return largestPrimeFactor(n / i);
    }
  }
};

// 56ms
const largestPrimeFactor = n => {
  if (n < 2) return n;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return largestPrimeFactor(i);
  }
  return n;
};

// 48ms
const largestPrimeFactor = n => {
  if (n < 2) return n;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      n = n / i;
      i = 2;
    } else {
      i++;
    }
  }
  return n;
};

// 50ms
const largestPrimeFactor = n => {
  if (n < 2) return n;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      n = n / i;
      i = 2;
    } else {
      i++;
    }
  }
  return n;
};

// 58ms
const largestPrimeFactor = n => {
  if (n < 2) return n;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      n = n / i;
      i = 2;