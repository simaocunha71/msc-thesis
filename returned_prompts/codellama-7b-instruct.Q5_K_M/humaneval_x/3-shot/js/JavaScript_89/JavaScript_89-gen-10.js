  let result = "";
  let alphabet = "abcdefghijklmnopqrstuvwxyz";
  let shift = 2 * 2;

  for (let i = 0; i < s.length; i++) {
    let index = alphabet.indexOf(s[i]);
    if (index == -1) {
      result += s[i];
    } else {
      index += shift;
      if (index >= alphabet.length) {
        index -= alphabet.length;
      }
      result += alphabet[index];
    }
  }
  return result;
}



