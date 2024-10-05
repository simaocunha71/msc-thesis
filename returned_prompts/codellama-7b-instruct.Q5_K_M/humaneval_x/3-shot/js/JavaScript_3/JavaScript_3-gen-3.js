  var balance = 0;

  for (const op of operations) {
    if (op > 0) {
      balance += op;
    } else {
      balance -= op;
    }
    if (balance < 0) {
      return true;
    }
  }

  return false;
}



