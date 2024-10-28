const sumProduct = (numbers) => {
  return numbers.length ? [numbers.reduce((a, b) => a + b, 0), numbers.reduce((a, b) => a * b, 1)] : [0, 1];
};

B:
const sumProduct = (numbers) => {
  return numbers.reduce(([s, p], n) => [s + n, p * n], [0, 1]);
};

C:
const sumProduct = (numbers) => {
  return numbers.reduce(([s, p], n) => [s + n, p * n], [0, 1]);
};

D:
const sumProduct = (numbers) => {
  const [sum, product] = numbers.reduce(([s, p], n) => [s + n, p * n], [0, 1]);
  return [sum, product];
};

E:
const sumProduct = (numbers) => {
  const [sum, product] = numbers.reduce(([s, p], n) => [s + n, p * n], [0, 1]);
  return [sum, product];
};

F:
const sumProduct = (numbers) => {
  const [sum, product] = numbers.reduce(([s, p], n) => [s + n, p * n], [0, 1]);
  return [sum, product];
};

G:
const sumProduct = (numbers) => {
  const [sum, product] = numbers.reduce(([s, p], n) => [s + n, p * n], [0, 1]);
  return [sum, product];
};

H:
const sumProduct = (numbers) => {
  const [sum, product] = numbers.reduce(([s, p], n) => [s + n, p * n], [0, 1]);
  return [sum, product];
};

I:
const sumProduct = (numbers) => {
  const [sum, product] = numbers.reduce(([s, p], n) => [s + n, p * n], [0, 1]);
  return [sum, product];
};

