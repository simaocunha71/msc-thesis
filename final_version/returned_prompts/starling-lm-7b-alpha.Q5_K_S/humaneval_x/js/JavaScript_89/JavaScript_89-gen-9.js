  let result = "";
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    let ascii = char.charCodeAt(0);
    if (ascii >= 65 && ascii <= 90) {
      result += String.fromCharCode((ascii - 65 + 2 * 2 * 2) % 26 + 65);
    } else if (ascii >= 97 && ascii <= 122) {
      result += String.fromCharCode((ascii - 97 + 2 * 2 * 2) % 26 + 97);
    } else {
      result += char;
    }
  }
  return result;
}



