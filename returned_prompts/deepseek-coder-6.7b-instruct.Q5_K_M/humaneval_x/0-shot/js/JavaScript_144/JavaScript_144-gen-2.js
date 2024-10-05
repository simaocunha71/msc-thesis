  // Split the fractions into numerators and denominators
  let [xNum, xDen] = x.split('/').map(Number);
  let [nNum, nDen] = n.split('/').map(Number);

  // Check if the product of the numerators is divisible by the product of the denominators
  return (xNum * nNum) % (xDen * nDen) === 0;
}

console.log(simplify("1/5", "5/1"));  // Outputs: true
console.log(simplify("1/6", "2/1"));  // Outputs: false
console.log(simplify("7/10", "10/2"));  // Outputs: false


This function firstly splits the given fractions into numerators and denominators. Then it checks if the product of the numerators is divisible by the product of the denominators. If it is, it returns true; otherwise it returns false.
*/


// You can test the function with the provided test cases
console.log(simplify("1/5", "5/1")); // Outputs: true
console.log(simplify("1/6", "2/1")); // Outputs: false
console.log(simplify("7/10", "10/2")); // Outputs: false

// Add more test cases to verify the function
console.log(simplify("1/2", "2/1")); // Outputs: true
console.log(simplify("2/3", "3/2")); // Outputs: true
console.log(simplify("3/4", "4/3")); // Outputs: true
console.log(simplify("4/5", "5/4")); // Outputs: true
console.log(simplify("5/6", "6/5")); // Outputs: true
console.log(simplify("6/7", "7/6")); // Outputs: true
console.log(simplify("7/8", "8/7")); // Outputs: true
console.log(simplify("8/9", "9/8")); // Outputs: true
console.