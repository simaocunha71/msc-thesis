  let balance = 0;
  for (const op of operations) {
    if (op < 0) {
      return true;
    }
    balance += op;
    if (balance < 0) {
      return true;
    }
  }
  return false;
}



