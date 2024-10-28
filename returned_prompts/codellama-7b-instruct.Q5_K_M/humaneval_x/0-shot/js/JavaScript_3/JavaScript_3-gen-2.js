const belowZero = (operations) => {
  let balance = 0;
  for (let i = 0; i < operations.length; i++) {
    if (balance < 0) return true;
    balance += operations[i];
  }
  return false;
};
