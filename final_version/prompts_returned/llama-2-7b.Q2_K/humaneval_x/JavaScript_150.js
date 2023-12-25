/*A simple program which should return the value of x if n is 
  a prime number and should return the value of y otherwise.

  Examples:
  for xOrY(7, 34, 12) == 34
  for xOrY(15, 8, 5) == 5
  
  */
const xOrY = (n, x, y) => {
  if (!y && n === 0) return 'Invalid Input!!';
  let result;
  
  //if you want to print the value in console.log()
  //console.log(x);
  
  for (let i = n + 1; i >= y + 1 ; i--){
    if (!isPrime(i)) break;
  }

  result = i - 2;
  if(!result) return 'Invalid Input!!';
  
  //if you want to print the value in console.log()
  console.log(`xOrY(${n}, ${y}, ${result})==> ${result}`);
  
  return result;
};

// function isPrime(number) {

// const n = number || '1';

// if (isNaN(n)) throw new Error('Not a Number!');

// if (!(n > 0 && n < Math.PI)) console.log(`Error: Not an integer ${n} and/or not a number.`);
// }
