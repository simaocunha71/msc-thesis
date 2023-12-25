/* Return list of prime factors of given integer in the order from smallest to largest.
  Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
  Input number should be equal to the product of all factors
  >>> factorize(8)
  [2, 2, 2]
  >>> factorize(25)
  [5, 5]
  >>> factorize(70)
  [2, 5, 7]
  */
const factorize = (n) => {
  let arr = [];
  for (let i = 2; i * i <= n; i++) {
    while (n % i == 0 && Math.floor(n / i) != -1) {
      if (Math.abs(i) > 1) {
        console.log('Factorizing: ' + strfactorize(n));
        arr = [...arr, ...strfactorize(n)];
        break;
      } else if (!!i && Math.floor(n / i) != -1)
        break;
    }
  }
  return arr;
};

const strfactorize = (n) => {
  let counter = [];
  for (let i = 2; i * i <= n; i++) {
    if (!!i && Math.floor(n / i) != -1) {
      counter = [...counter, ...strfactorize(n)];
      break;
    } else
      for (let j = 0; j < counter.length; j++)
        if (!!i && Math.floor(n / i * counter[j]) != -1) {
          counter = [...counter, ...strfactorize(n)];
          break;
        } else
          counter = [
            ...counter, // all previous counter values
            Math.abs(counter.length == 0 ? (parseInt(n / i)), n / i),
            parseInt(n / i)
          ];
      if (!!i && Math.floor(n / i * counter[j]) != -1) {
        counter = [
          ...counter, // all previous counter values
          Math.abs(counter[j] == 0 ?