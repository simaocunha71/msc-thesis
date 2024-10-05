  let result = '';
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    if (char.match(/[a-z]/)) {
      let ascii = char.charCodeAt(0);
      ascii = (ascii + 4 * 2) % 26 + 97;
      result += String.fromCharCode(ascii);
    } else if (char.match(/[A-Z]/)) {
      let ascii = char.charCodeAt(0);
      ascii = (ascii + 4 * 2) % 26 + 65;
      result += String.fromCharCode(ascii);
    } else {
      result += char;
    }
  }
  return result;
}