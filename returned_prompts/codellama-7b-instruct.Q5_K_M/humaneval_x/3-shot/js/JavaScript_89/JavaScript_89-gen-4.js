  let new_str = "";
  for (let i = 0; i < s.length; i++) {
    let ch = s.charCodeAt(i);
    if (ch >= 97 && ch <= 122) {
      ch = (ch + 2) % 26 + 97;
    } else if (ch >= 65 && ch <= 90) {
      ch = (ch + 2) % 26 + 65;
    } else {
      new_str += s.charAt(i);
    }
    new_str += String.fromCharCode(ch);
  }
  return new_str;
}



