/*Return the largest prime factor of n. Assume n > 1 and is not a prime.
  >>> largestPrimeFactor(13195)
  29
  >>> largestPrimeFactor(2048)
  2
  */
const largestPrimeFactor = (n) => {
  let numFactors = 0;
  for (let i in n) {
    if (n % i === 0 && (i === 1 || (i > 1 && n / i < 2))) {
      numFactors += 1;
    }
  }
  return Math.max(...(numFactors).map((i) => Math.floor(Math.sqrt(n))));
};

/*Print all numbers divisible by 3 from 1 to n, assume that n > 1 and is not a prime */
const printDivisiblesByThree = (number, currentCount, totalCount) => {
  if (!currentCount || !currentCount.includes(number)) {
    console.log(`${number}`, ' ', number);
    currentCount.push(number);
    number++;

    if (number > totalCount) return;

    printDivisiblesByThree(number, currentCount, totalCount - 1);
  } else {
    console.log(`${currentCount[currentCount.length - 1]} `, ' ', number);
  }
};

const divisibleby3 = (n) =>
{
    let currentCount = [],
        totalCount = 0;
    if(!isNaN(n)) n++;
    printDivisiblesByThree(n, currentCount, totalCount);
}

const main = () => {
  console.log("3");
  divisibleby3(841);
}
main();
