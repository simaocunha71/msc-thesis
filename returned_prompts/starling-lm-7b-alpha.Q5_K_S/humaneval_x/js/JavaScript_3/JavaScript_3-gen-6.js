  let balance = 0;
  for (const o of operations) {
    if (o < 0) {
      return true;
    } else {
      balance += o;
    }
    if (balance < 0) {
      return true;
    }
  }
  return false;
}



