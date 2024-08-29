  let result = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] != c) {
      result += s[i];
    }
  }
  let reversed = result.split("").reverse().join("");
  return [reversed, result === reversed];
}



