  let result = '';
  for (let i = 0; i < s.length; i++) {
    let charCode = s.charCodeAt(i);
    if (charCode >= 65 && charCode <= 90) {
      result += String.fromCharCode((charCode - 65 + (2 * 2)) % 26 + 65);
    } else if (charCode >= 97 && charCode <= 122) {
      result += String.fromCharCode((charCode - 97 + (2 * 2)) % 26 + 97);
    } else {
      result += s[i];
    }
  }
  return result;
}