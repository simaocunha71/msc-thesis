  const collatz = (num) => {
    if (num === 1) return 1;
    if (num % 2 === 0) return collatz(num / 2);
    return collatz(3 * num + 1);
  };

  const getOdd = (num) => {
    const arr = [];
    while (num !== 1) {
      arr.push(num);
      num = collatz(num);
    }
    return arr;
  };

  const isOdd = (num) => num % 2 === 1;

  return getOdd(n).filter(isOdd);
}
