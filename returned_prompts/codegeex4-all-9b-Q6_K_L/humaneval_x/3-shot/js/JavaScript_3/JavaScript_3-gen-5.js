  var balance = 0;

  for (const amount of operations) {
    balance += amount;
    if (balance < 0) {
      return true;
    }
  }

  return false;
}



