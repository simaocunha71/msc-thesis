  let fibArr = [2, 3];
  let i = 2;

  while (fibArr.length < n) {
    let fibNum = fibArr[i - 1] + fibArr[i - 2];
    let isPrime = true;
    for (let j = 2, s = Math.sqrt(fibNum); j <= s; j++)
      if (fibNum % j === 0) isPrime = false;
    if (isPrime) fibArr.push(fibNum);
    i++;
  }

  return fibArr[n - 1];
};
*/

const primeFib = (n) => {
  let fibArr = [2, 3];
  let i = 2;

  while (fibArr.length < n) {
    let fibNum = fibArr[i - 1] + fibArr[i - 2];
    let isPrime = true;
    for (let j = 2, s = Math.sqrt(fibNum); j <= s; j++)
      if (fibNum % j === 0) isPrime = false;
    if (isPrime) fibArr.push(fibNum);
    i++;
  }

  return fibArr[n - 1];
};

console.log(primeFib(1)); // 2
console.log(primeFib(2)); // 3
console.log(primeFib(3)); // 5
console.log(primeFib(4)); // 13
console.log(primeFib(5)); // 89
console.log(primeFib(6)); // 233
console.log(primeFib(7)); // 1597
console.log(primeFib(8)); // 28657
console.log(primeFib(9)); // 514229
console.log(primeFib(10)); // 433494437
console.log(primeFib(11)); // 267914296
console