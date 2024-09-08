  let balance = 0;
  for (const operation of operations) {
    balance += operation;
    if (balance < 0) {
      return true;
    }
  }
  return false;
}



