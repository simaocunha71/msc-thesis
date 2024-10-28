const belowZero = (operations) => {
let balance = 0;
for (let i = 0; i < operations.length; i++) {
  const currentOperation = operations[i];
  balance += currentOperation;
  if (balance < 0) {
    return true;
  }
}
return false;
};

