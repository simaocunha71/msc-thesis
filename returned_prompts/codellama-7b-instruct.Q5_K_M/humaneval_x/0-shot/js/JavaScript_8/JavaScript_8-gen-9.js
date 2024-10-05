const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
  for (const number of numbers) {
    sum += number;
    product *= number;
  }
  return [sum, product];
};

B:
const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
  numbers.forEach(number => {
    sum += number;
    product *= number;
  });
  return [sum, product];
};

C:
const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
  numbers.map(number => {
    sum += number;
    product *= number;
  });
  return [sum, product];
};

D:
const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }
  return [sum, product];
};

E:
const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
  while (numbers.length !== 0) {
    sum += numbers[0];
    product *= numbers[0];
    numbers.shift();
  }
  return [sum, product];
};

F:
const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
  for (const number of numbers) {
    sum += number;
    product *= number;
  }
  return [sum, product];
};

G:
const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
  for (const number of numbers) {
    sum += number;
    product *= number;
  }
  return [sum, product];
};

H:
const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
 