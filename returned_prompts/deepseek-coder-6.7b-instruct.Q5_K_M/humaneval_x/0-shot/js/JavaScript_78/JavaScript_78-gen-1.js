  const primes = new Set([2, 3, 5, 7, 11, 13]);
  let count = 0;

B:
  for (let c of num) {

C:
    let digit = parseInt(c, 16);
    if (primes.has(digit)) {
      count += 1;
    }
  }

D:
  return count;
};

module.exports = hexKey;
E:
  console.log(hexKey("AB")); //1
  console.log(hexKey("1077E")); //2
  console.log(hexKey("ABED1A33")); //4
  console.log(hexKey("123456789ABCDEF0")); //6
  console.log(hexKey("2020")); //2
  ```





























































































