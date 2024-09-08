  let binary = decimal.toString(2);
  binary = 'db' + binary.padStart(binary.length + 1, '0') + 'db';
  return binary;
}



