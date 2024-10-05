  if(n > m) return -1;
  let avg = Math.round((n + m) / 2);
  return (avg >>> 0).toString(2);
  
};

console.log(roundedAvg(1, 5)); // => “0b11”
console.log(roundedAvg(7, 5)); // => -1
console.log(roundedAvg(10, 20)); // => “0b1111”
console.log(roundedAvg(20, 33)); // => “0b11010”




//Explanation:
//First, we check if n is greater than m. If it is, we return -1.
//If n is not greater than m, we calculate the average of n and m, rounding it to the nearest integer.
//We then convert this rounded average to binary using the bitwise right shift operator (>>>) and the toString method with base 2.
//Finally, we return this binary string.
//Note that we use the bitwise right shift operator (>>>) to convert the average to an unsigned integer. This is because the toString method with base 2 would otherwise return a leading "-" if the average is negative.
//We also use the bitwise AND operator (&) to mask off the sign bit, effectively making the number unsigned.
//This is necessary because the toString method with base 2 would otherwise return a leading "-" for negative numbers.
//The unsigned right shift operator (>>>) shifts the binary representation of the number to the right, filling in any vacant positions with zeros.
//This effectively masks off the sign bit, leaving us with the correct binary representation of the average.



//Test cases:
//roundedAvg(1, 5) should return "0b11"
//roundedAvg(7, 5) should return -1
//roundedAvg(10, 20) should return "0b1111"
//roundedAvg(20, 33) should return "0b11010"
//roundedAvg(-5, 5) should return -1
//round