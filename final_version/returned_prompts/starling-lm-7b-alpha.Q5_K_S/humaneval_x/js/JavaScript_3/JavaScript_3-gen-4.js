  let balance = 0;
  for (let op of operations) {
    if (op < 0) {
      balance += op;
      if (balance < 0) {
        return true;
      }
    } else {
      balance -= op;
    }
  }
  return false;
}



