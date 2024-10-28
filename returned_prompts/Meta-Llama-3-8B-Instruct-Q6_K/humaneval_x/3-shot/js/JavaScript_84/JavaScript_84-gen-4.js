  let binary = N.toString(2);
  let sum = 0;
  for (let i = 0; i < binary.length; i++) {
    sum += parseInt(binary[i]);
  }
  return binary;
}  // This is not correct. It's supposed to return the sum of digits in binary form of N not the binary representation of N. 

const solve = (N) => {
  let sum = 0;
  let binary = N.toString(2);
  for (let i = 0; i < binary.length; i++) {
    sum += parseInt(binary[i]);
  }
  return sum.toString();
}  // This is correct. It returns the sum of digits in binary form of N. 





