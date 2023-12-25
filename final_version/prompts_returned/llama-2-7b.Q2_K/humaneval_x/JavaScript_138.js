/*Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
  Example
  isEqualToSumEven(4) == false
  isEqualToSumEven(6) == false
  isEqualToSumEven(8) == true
  */
const isEqualToSumEven = (n) => {
  if ((n % 2) === 0 && n % 6 !== 0) return false;
}

/*
Solution of Day 16 - https://adventofcode.com/2017/day/16
 */
const partOne = (input, n) => {
    const sumOfOddDigits = 0n;
    for(let i=0;i<input.length-n;++i){
        let remainder = input[i]%2n;
        if(!isEqualToSumEven(remainder)){
            return false;
        } else {
            sumOfOddDigits += remainder;
        }
    }
    return n === sumOfOddDigits;
}

const partTwo = (input, n) => {
  let sumOfEvenDigits = (0), remainder;
  for(let i=0;i<input.length-n;++i){
      remainder = input[i]%2n+1n;
      if(!isEqualToSumEven(remainder)){
        return false;
      } else {
          sumOfEvenDigits += remainder;
      }
  }
  return isEqualToSumEven(sumOfOddDigits) && isEqualToSumEven(sumOfEvenDigits);
}
console.log(`isPartOne(${partOne.toString()})` );
console.log(`isPartTwo(${partTwo.toString()})`);