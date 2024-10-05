const evenOddCount = (num) => {
  const numStr = num.toString();
  return [numStr.split('').filter(x => x % 2 === 0).length, numStr.split('').filter(x => x % 2 !== 0).length];
};

