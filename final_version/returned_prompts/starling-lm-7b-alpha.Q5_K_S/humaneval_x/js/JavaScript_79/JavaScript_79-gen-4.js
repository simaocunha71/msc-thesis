  let binary = '1' + decimal.toString(2);
  let result = '';
  while (binary.length > 1) {
    result = 'db' + binary.charAt(binary.length - 2) + result + 'db';
    binary = binary.slice(1);
  }

  return result;
}



