  let binary = decimal.toString(2);
  return 'db' + Array(Math.ceil((binary.length + 3) / 8) * 8 - binary.length).join('0') + binary + 'db';
}