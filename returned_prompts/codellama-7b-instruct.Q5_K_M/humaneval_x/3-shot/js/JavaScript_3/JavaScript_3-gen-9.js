  var balance = 0;

  for (const o of operations) {
    if (o < 0) {
      balance += o;
      if (balance < 0) return true;
    } else {
      balance += o;
    }
  }

  return false;
}



