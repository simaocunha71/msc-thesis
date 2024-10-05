  if (n < 8) return false;
  if (n % 2 != 0) return false;
  return true;
};

console.log(isEqualToSumEven(4)); // false
console.log(isEqualToSumEven(6)); // false
console.log(isEqualToSumEven(8)); // true
console.log(isEqualToSumEven(10)); // true
console.log(isEqualToSumEven(12)); // true
console.log(isEqualToSumEven(14)); // true
console.log(isEqualToSumEven(16)); // true
console.log(isEqualToSumEven(18)); // true
console.log(isEqualToSumEven(20)); // true

