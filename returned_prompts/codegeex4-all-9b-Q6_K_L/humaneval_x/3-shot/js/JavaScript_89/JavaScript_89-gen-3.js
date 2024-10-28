  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let result = '';
  for (let c of s) {
    let index = alphabet.indexOf(c);
    if (index != -1) {
      result += alphabet[(index + 4) % 26];
    } else {
      result += c;
    }
  }
  return result;
}



