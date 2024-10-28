
const primeNumbers = [];
const primeNumbersDigits = [];

lst.forEach((element) => {
  if (element > 1) {
    for (let i = 2; i < element; i += 1) {
      if (element % i === 0) {
        return;
      }
    }
    primeNumbers.push(element);
  }
});

primeNumbers.forEach((element) => {
  primeNumbersDigits.push(element.toString().split('').reduce((a, b) => Number(a) + Number(b)));
});

return primeNumbersDigits.reduce((a, b) => a + b);
};

module.exports = skjkasdkd;
