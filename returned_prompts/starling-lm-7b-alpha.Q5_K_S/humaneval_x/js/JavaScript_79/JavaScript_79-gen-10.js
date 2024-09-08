  let binary = decimal.toString(2);
  return "db" + "0".repeat(7 - binary.length) + binary + "db";
}



