/*Write a function that takes a string and returns true if the string
  length is a prime number or false otherwise
  Examples
  primeLength('Hello') == true
  primeLength('abcdcba') == true
  primeLength('kittens') == true
  primeLength('orange') == false
  */
  const primeLength = (string) => {
    const stringLength = string.length;
    for (let i = 2; i < stringLength; i++) {
      if (stringLength % i === 0) {
        return false;
      }
    }
    return true;
  }

//  if (stringLength === 0) return false;
//  for (let i = 2; i < stringLength; i++) {
//    if (stringLength % i === 0) return false;
//  }
//  return true;

//  let isPrime = true;
//  for (let i = 2; i < stringLength; i++) {
//    if (stringLength % i === 0) {
//      isPrime = false;
//      break;
//    }
//  }
//  return isPrime;

//  for (let i = 2; i < stringLength; i++) {
//    if (stringLength % i === 0) return false;
//  }
//  return true;

//  let prime = true;
//  for (let i = 2; i < stringLength; i++) {
//    if (stringLength % i === 0) {
//      prime = false;
//      break;
//    }
//  }
//  return prime;

//  let prime = true;
//  for (let i = 2; i < stringLength; i++) {
//    if (stringLength % i === 0) {
//      prime = false;
//      break;
//    }
//  }
//  return prime;

//  for (let i = 2; i < stringLength; i++) {
//    if (stringLength % i === 0) return false;
//  }
//  return true;

//  for (