  let balance = 0;
  for (const operation of operations) {
    balance += operation;
    if (balance < 0) {
      return true;
    }
  }
  return false;
}  // This function works by iterating through the list of operations, adding each one to the balance,
    // and checking if the balance ever falls below zero. If it does, the function returns true.
    // If the function finishes iterating through the list without the balance ever falling below zero,
    // it returns false.