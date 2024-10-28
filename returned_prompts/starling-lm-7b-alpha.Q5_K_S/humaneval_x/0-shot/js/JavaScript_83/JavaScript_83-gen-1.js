/*
  Given a positive integer n, return the count of the numbers of n-digit
  positive integers that start or end with 1.
  */
const startsOneEnds = (n) => {
    if (n === 1) return 2;
    const half = Math.pow(10, Math.floor(n / 2));
    return 9 * half + (half - Math.pow(10, n - 1)) / 10;
};

console.log(startsOneEnds(1)); // 2
console.log(startsOneEnds(2)); // 3
console.log(startsOneEnds(3)); // 6
console.log(startsOneEnds(4)); // 10
console.log(startsOneEnds(5)); // 15
console.log(startsOneEnds(6)); // 21
console.log(startsOneEnds(7)); // 28
console.log(startsOneEnds(8)); // 36
console.log(startsOneEnds(9)); // 45
console.log(startsOneEnds(10)); // 55

*/

*/

