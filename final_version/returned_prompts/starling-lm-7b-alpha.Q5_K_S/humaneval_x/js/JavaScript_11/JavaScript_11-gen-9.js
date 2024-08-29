  let result = '';
  for (let i = 0; i < a.length; i++) {
    let char_a = a[i];
    let char_b = b[i];
    let char_result = '';
    if (char_a == '1' && char_b == '1') {
      char_result = '0';
    } else if (char_a == '0' && char_b == '0') {
      char_result = '0';
    } else if (char_a == '1' && char_b == '0') {
      char_result = '1';
    } else if (char_a == '0' && char_b == '1') {
      char_result = '1';
    }
    result += char_result;
  }

  return result;
}



