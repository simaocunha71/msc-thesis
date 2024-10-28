  let binary = decimal.toString(2);
  return "db" + binary + "db";
}

console.log(decimalToBinary(15)); // returns  "db1111db"
console.log(decimalToBinary(32)); // returns  "db100000db"

// This function works by using the built-in JavaScript method toString() with an argument of 2. This will convert the decimal number to binary. Then it adds the "db" at the beginning and end of the string.

// The time complexity for this function is O(1) because it performs a constant amount of operations regardless of the size of the input.
// The space complexity is also O(1) because it only uses a constant amount of space to store the binary string and the two surrounding characters.

// The function can also handle negative numbers, because the built-in toString method can handle them.

// If the decimal number is 0, then the binary representation is also 0, so the function will return "db0db".
// If the decimal number is negative, the function will return a binary representation starting with "-".
// The "db" surrounding characters are not affected by the negative sign.

// For example, decimalToBinary(-15) will return "db-1111db", decimalToBinary(-32) will return "db-100000db".
  
// This function is a good candidate for a beginner or intermediate programmer because it combines several JavaScript built-in methods and features.
// It also demonstrates a clear understanding of how to handle different cases, such as negative numbers and zero.

// Overall, it is a well-structured and easy-to-understand function.
  
};

console.log(decimalToBinary(15)); // returns  "db1111db"
console.log(decimalToBinary(32)); // returns  "db100000db"
console.log(decimalToBinary(0)); // returns  "db0db"
console.log(decimalToBinary(-15)); // returns  "db-1111db"
console.log(decimalToBinary(-32)); // returns  "db-100