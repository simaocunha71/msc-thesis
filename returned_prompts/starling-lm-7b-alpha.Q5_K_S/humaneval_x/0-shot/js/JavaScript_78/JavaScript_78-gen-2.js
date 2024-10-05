
  // your solution goes here
  let hexKey = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
  };

  let result = 0;

  for (let i = 0; i < num.length; i++) {
    let n = hexKey[num[i]];
    if (isPrime(n)) {
      result++;
    }
  }

  return result;
};

function isPrime(n) {
  if (n < 2) return false;
  if (n === 2) return true;
  if (n % 2 === 0) return false;
  for (let i = 3; i * i <= n; i += 2) {
    if (n % i === 0) return false;
  }
  return true;
}

console.log(hexKey("AB"));
console.log(hexKey("1077E"));
console.log(hexKey("ABED1A33"));
console.log(hexKey("123456789ABCDEF0"));
console.log(hexKey("2020"));

*/





















































































































