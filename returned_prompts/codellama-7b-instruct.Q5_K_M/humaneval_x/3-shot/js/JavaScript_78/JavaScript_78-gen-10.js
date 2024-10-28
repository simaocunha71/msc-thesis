  var result = 0;
  const hex_array = num.split('');

  for (const hex of hex_array) {
    if (hex == 'A') {
      result += 10;
    } else if (hex == 'B') {
      result += 11;
    } else if (hex == 'C') {
      result += 12;
    } else if (hex == 'D') {
      result += 13;
    } else if (hex == 'E') {
      result += 14;
    } else if (hex == 'F') {
      result += 15;
    } else {
      result += parseInt(hex);
    }
  }

  return result;
}



