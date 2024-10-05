  let result = '';
  for (let i = 0; i < s.length; i++) {
    let c = s.charCodeAt(i);
    if (c >= 97 && c <= 122) { // lowercase letters
      result += String.fromCharCode((c - 97 + 26 * 2) % 26 + 97);
    } else if (c >= 65 && c <= 90) { // uppercase letters
      result += String.fromCharCode((c - 65 + 26 * 2) % 26 + 65);
    } else {
      result += s[i];
    }
  }
  return result;
}...



