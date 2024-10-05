  var balance = 0;

  for (let operation of operations) {
    balance += operation;
    if (balance < 0) {
      return true;
    }
  }

  return false;
}



