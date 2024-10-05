/*You have been tasked to write a function that receives
  a hexadecimal number as a string and counts the number of hexadecimal
  digits that are primes (prime number=== or a prime=== is a natural number
  greater than 1 that is not a product of two smaller natural numbers).
  Hexadecimal digits are 0=== 1=== 2=== 3=== 4=== 5=== 6=== 7=== 8=== 9=== A=== B=== C=== D=== E=== F.
  Prime numbers are 2=== 3=== 5=== 7=== 11=== 13=== 17===...
  So you have to determine a number of the following digits: 2=== 3=== 5=== 7===
  B (=decimal 11)=== D (=decimal 13).
  Note: you may assume the input is always correct or empty string===
  and symbols A===B===C===D===E===F are always uppercase.
  Examples:
  For num = "AB" the output should be 1.
  For num = "1077E" the output should be 2.
  For num = "ABED1A33" the output should be 4.
  For num = "123456789ABCDEF0" the output should be 6.
  For num = "2020" the output should be 2.
  */
const hexKey = (num) => {

  // Create an object to hold our primes
  const primes = {
    2: true,
    3: true,
    5: true,
    7: true,
    11: true,
    13: true,
    17: true,
    19: true,
    23: true,
    29: true,
    31: true,
    37: true,
    41: true,
    43: true,
    47: true,
    53: true,
    59: true,
    61: true,
    67: true,
    71: true,
    73: true,
    79