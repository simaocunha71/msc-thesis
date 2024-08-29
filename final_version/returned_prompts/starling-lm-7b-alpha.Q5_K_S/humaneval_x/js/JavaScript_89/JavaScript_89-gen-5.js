  let result = "";
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  for (const c of s) {
    let i = alphabet.indexOf(c);
    if (i == -1) {
      result += c;
    } else {
      result += alphabet[(i + 2 * 2) % alphabet.length];
    }
  }
  return result;
}



