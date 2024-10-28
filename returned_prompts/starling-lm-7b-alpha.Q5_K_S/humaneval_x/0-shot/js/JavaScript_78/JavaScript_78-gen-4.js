  let hexNumber = [];
  let hexPrimes = [];
  let count = 0;

  if (num === '') {
    return 0;
  }

  while (num > 0) {
    hexNumber.push(num % 16);
    num = parseInt(num / 16);
  }

  hexNumber.reverse();

  for (let i = 0; i < hexNumber.length; i++) {
    if (hexNumber[i] <= 9) {
      if (hexNumber[i] === 2 || hexNumber[i] === 3 || hexNumber[i] === 5 || hexNumber[i] === 7) {
        hexPrimes.push(hexNumber[i]);
        count += 1;
      }
    } else if (hexNumber[i] >= 10 && hexNumber[i] <= 15) {
      if (hexNumber[i] === 11 || hexNumber[i] === 13) {
        hexPrimes.push(hexNumber[i]);
        count += 1;
      }
    }
  }

  return count;
}

//Test
console.log(hexKey('AB'));
console.log(hexKey('1077E'));
console.log(hexKey('ABED1A33'));
console.log(hexKey('123456789ABCDEF0'));
console.log(hexKey('2020'));






























































































































































