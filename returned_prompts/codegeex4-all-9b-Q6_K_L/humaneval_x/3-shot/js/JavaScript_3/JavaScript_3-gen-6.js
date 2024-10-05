  let balance = 0;

  for (const o of operations) {
    balance += o;
    if (balance < 0) {
      return true;
    }
  }

  return false;
}



