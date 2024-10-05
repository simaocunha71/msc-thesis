  let balance = 0;
  for (let i = 0; i < operations.length; i++) {
    if (operations[i] < 0) {
      balance += operations[i];
    } else {
      balance -= operations[i];
    }
    if (balance < 0) {
      return true;
    }
  }
  return false;
}