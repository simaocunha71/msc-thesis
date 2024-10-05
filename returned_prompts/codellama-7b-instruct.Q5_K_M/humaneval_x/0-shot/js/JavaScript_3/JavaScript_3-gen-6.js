
// You can simply track the balance of the account and check if it ever goes below zero.
// For example:
const belowZero = (operations) => {
  let balance = 0;
  for (const operation of operations) {
    balance += operation;
    if (balance < 0) return true;
  }
  return false;
};

