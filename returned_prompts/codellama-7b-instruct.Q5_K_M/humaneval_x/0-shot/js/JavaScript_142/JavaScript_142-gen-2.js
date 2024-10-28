
const sumSquares = (lst) => {
  let result = 0;
  for(let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) {
      result += Math.pow(lst[i], 2);
    } else if (i % 4 === 0 && !(i % 3 === 0)) {
      result += Math.pow(lst[i], 3);
    } else {
      result += lst[i];
    }
  }
  return result;
}

const sumSquares = (lst) => lst.map((v, i) => (i % 3 === 0 ? Math.pow(v, 2) : i % 4 === 0 ? Math.pow(v, 3) : v)).reduce((a, b) => a + b, 0);

const sumSquares = lst => lst.reduce((sum, num) => {
  const isMultipleOfThree = num % 3 === 0;
  const isMultipleOfFour = num % 4 === 0;

  if (isMultipleOfThree && !isMultipleOfFour) {
    sum += Math.pow(num, 3);
  } else if (isMultipleOfFour && !isMultipleOfThree) {
    sum += Math.pow(num, 2);
  } else {
    sum += num;
  }

  return sum;
}, 0);

const sumSquares = (lst) => lst.reduce((a, b) => a + (b % 3 ? b : b * b), 0);

const sumSquares = (lst) => lst.map((v, i) => (i % 3 === 0 ? v ** 2 : i % 4 === 0 ? v ** 3 : v)).reduce((a, b) => a + b, 0);

const sumSquares = (lst) => lst.map((v, i) => (i % 3 === 0 ? v ** 2 : i % 4 === 0 ? v ** 3 : v)).reduce((a, b)