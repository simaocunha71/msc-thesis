  let digits = Array.from(String(n), Number);
  let odd = digits.filter(digit => digit % 2 !== 0);
  return odd.length === 0 ? 0 : odd.reduce((a, b) => a * b);
}

console.log(digits(1));  // 1
console.log(digits(4));  // 0
console.log(digits(235));  // 15

/*
In this solution, we start by converting the number to an array of digits.
We then filter this array to include only the odd digits. If there are no odd digits, we return 0. If there are odd digits, we reduce this array to a product and return this product.
*/


//Alternate Solution

const digits = n => {
  let product = 1, foundOdd = false;
  for(let i of Array.from(String(n), Number)) {
    if(i % 2 !== 0) {
      product *= i;
      foundOdd = true;
    }
  }
  return foundOdd ? product : 0;
}

console.log(digits(1));  // 1
console.log(digits(4));  // 0
console.log(digits(235));  // 15

/*
This solution is a bit more efficient because it only has to loop through the digits once.
It also uses a bit more efficient way to create the product.
*/

//Alternate Solution

const digits = n => {
  let str = String(n);
  let product = 1, foundOdd = false;
  for(let i = 0; i < str.length; i++) {
    let digit = Number(str[i]);
    if(digit % 2 !== 0) {
      product *= digit;
      foundOdd = true;
    }
  }
  return foundOdd ? product : 0;
}

console.log(digits(1));  // 1
console.log(digits(4));  // 0
console.