  return arr.sort((a, b) => {
    if (a % 2 === 0 && b % 2 !== 0) return -1;
    if (a % 2 !== 0 && b % 2 === 0) return 1;
    if ((a >>> 0).toString(2).split('1').length - 1 === (b >>> 0).toString(2).split('1').length - 1) {
      return a - b;
    }
    return (a >>> 0).toString(2).split('1').length - 1 - (b >>> 0).toString(2).split('1').length - 1;
  });
}
// Explanation:
// 1. First, we sort the array based on the number of 1's in their binary representation.
//    We use bitwise operations to get the binary representation of the numbers and count the number of 1's.
//    If the numbers have the same number of 1's, we sort them based on their decimal values.