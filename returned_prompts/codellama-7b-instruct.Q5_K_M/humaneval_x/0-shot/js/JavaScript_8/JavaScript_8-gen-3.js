const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }
  return [sum, product];
}

B:
const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }
  return [sum, product];
}

C:
const sumProduct = (numbers) => {
  return [
    numbers.reduce((a, b) => a + b, 0),
    numbers.reduce((a, b) => a * b, 1)
  ];
}

D:
const sumProduct = (numbers) => {
  return [
    numbers.reduce((sum, num) => sum + num, 0),
    numbers.reduce((product, num) => product * num, 1)
  ];
}

E:
const sumProduct = (numbers) => {
  return [
    numbers.reduce((sum, num) => sum + num, 0),
    numbers.reduce((product, num) => product * num, 1)
  ];
}

F:
const sumProduct = (numbers) => {
  return [
    numbers.reduce((sum, num) => sum + num, 0),
    numbers.reduce((product, num) => product * num, 1)
  ];
}

G:
const sumProduct = (numbers) => {
  return [
    numbers.reduce((sum, num) => sum + num, 0),
    numbers.reduce((product, num) => product * num, 1)
  ];
}

H:
const sumProduct = (numbers) => {
  return [
    numbers.reduce((sum, num) => sum + num, 0),
    numbers.reduce((product, num) => product * num, 1)
  ];
}

I:
