  return [numbers.reduce((a, b) => a + b, 0), numbers.reduce((a, b) => a * b, 1)];
}

const sumProduct = (numbers) => {

B:
  return numbers.reduce(([sum, product], current) => {
    return [sum + current, product * current];
  }, [0, 1]);
}

const sumProduct = (numbers) => {

C:
  return numbers.reduce((sum, product, index) => {
    return [sum + numbers[index], product * numbers[index]];
  }, [0, 1]);
}

const sumProduct = (numbers) => {

D:
  let sum = 0;
  let product = 1;
  for (const number of numbers) {
    sum += number;
    product *= number;
  }
  return [sum, product];
}

const sumProduct = (numbers) => {

E:
  const sum = numbers.reduce((a, b) => a + b, 0);
  const product = numbers.reduce((a, b) => a * b, 1);
  return [sum, product];
}

const sumProduct = (numbers) => {

F:
  let sum = 0;
  let product = 1;
  for (const number of numbers) {
    sum += number;
    product *= number;
  }
  return [sum, product];
}
