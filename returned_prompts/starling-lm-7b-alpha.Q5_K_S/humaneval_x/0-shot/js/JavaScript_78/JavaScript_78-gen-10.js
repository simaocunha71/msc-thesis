  let n = num;
  let hexadecimalPrimeCount = 0;
  let hexadecimalPrime = [];
  let hexadecimalPrimeNum = [];
  let prime = [2, 3, 5, 7, 11, 13, 17];

  if (n == "") {
    console.log(hexadecimalPrimeCount);
    return;
  }

  for (let i = 0; i < n.length; i++) {
    let digit = Number(n[i]);
    if (digit >= 0 && digit <= 9) {
      for (let j = 0; j < prime.length; j++) {
        if (prime[j] == digit) {
          hexadecimalPrime.push(prime[j]);
          hexadecimalPrimeCount++;
          break;
        }
      }
    } else if (digit >= 10 && digit <= 15) {
      let hex = String(digit);
      if (hex == "A") {
        hexadecimalPrime.push(11);
        hexadecimalPrimeCount++;
      } else if (hex == "B") {
        hexadecimalPrime.push(13);
        hexadecimalPrimeCount++;
      } else if (hex == "C") {
        hexadecimalPrime.push(17);
        hexadecimalPrimeCount++;
      } else if (hex == "D") {
        hexadecimalPrime.push(19);
        hexadecimalPrimeCount++;
      } else if (hex == "E") {
        hexadecimalPrime.push(23);
        hexadecimalPrimeCount++;
      } else if (hex == "F") {
        hexadecimalPrime.push(29);
        hexadecimalPrimeCount++;
      }
    }
  }

  console.log(hexadecimalPrimeCount);
  return;
};

hexKey(String(prompt()));

*/









