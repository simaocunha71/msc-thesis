/* You're given a list of deposit and withdrawal operations on a bank account that starts with
  zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
  at that point function should return true. Otherwise it should return false.
  >>> belowZero([1, 2, 3])
  false
  >>> belowZero([1, 2, -4, 5])
  true
  */
const belowZero = (operations) => {
  let sum = operations.reduce((acc, cur) => acc + cur, 0);
  return sum < 0;
};
