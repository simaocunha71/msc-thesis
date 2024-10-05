  var result = 1;
  for (const c of n.toString()) {
    if (c % 2 == 1) {
      result *= parseInt(c);
    }
  }
  return result;
}



