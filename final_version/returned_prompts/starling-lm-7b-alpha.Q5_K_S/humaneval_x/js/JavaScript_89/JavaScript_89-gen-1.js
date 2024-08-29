  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  const rotated_alphabet = alphabet.slice(2).concat(alphabet.slice(0, 2));

  let result = "";
  for (const c of s) {
    if (c === ' ') {
      result += c;
    } else {
      result += rotated_alphabet[alphabet.indexOf(c)];
    }
  }
  return result;
}



