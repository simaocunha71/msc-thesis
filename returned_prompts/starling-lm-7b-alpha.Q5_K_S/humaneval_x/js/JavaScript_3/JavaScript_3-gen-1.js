  let balance = 0;
  for (const operation of operations) {
    if (operation > 0) {
      balance += operation;
    } else {
      balance += operation;
      if (balance < 0) {
        return true;
      }
    }
  }
  return false;
}



