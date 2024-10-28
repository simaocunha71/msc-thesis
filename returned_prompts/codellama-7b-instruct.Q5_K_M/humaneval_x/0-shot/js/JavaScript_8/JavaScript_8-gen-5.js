const sumProduct = (numbers = []) => {
    let sum = 0;
    let product = 1;
    numbers.forEach(n => {
      sum += n;
      product *= n;
    });
    return [sum, product];
  };
  console.log(sumProduct([])); // [0, 1]
  console.log(sumProduct([1, 2, 3, 4])); // [10, 24]
  console.log(sumProduct([1, 2, 3, 4, 5])); // [15, 120]
  console.log(sumProduct([1, 2, 3, 4, 5, 6])); // [21, 720]

B:
const sumProduct = (numbers = []) => {
    let sum = 0;
    let product = 1;
    if(numbers.length === 0) {
      return [0, 1];
    }
    numbers.forEach(n => {
      sum += n;
      product *= n;
    });
    return [sum, product];
  };
  console.log(sumProduct([])); // [0, 1]
  console.log(sumProduct([1, 2, 3, 4])); // [10, 24]
  console.log(sumProduct([1, 2, 3, 4, 5])); // [15, 120]
  console.log(sumProduct([1, 2, 3, 4, 5, 6])); // [21, 720]

C:
const sumProduct = (numbers = []) => {
    let sum = 0;
    let product = 1;
    if(numbers.length === 0) {
      return [0, 1];
    }
    numbers.forEach(n => {
      sum += n;
      product *= n;
    });
    return [sum, product];
  };
  console.log(sumProduct([])); // [0, 1]
  console.log(sumProduct([