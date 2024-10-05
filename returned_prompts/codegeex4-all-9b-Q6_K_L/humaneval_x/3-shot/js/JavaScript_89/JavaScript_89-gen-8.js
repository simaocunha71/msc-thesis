  let result = '';
  for (let i = 0; i < s.length; i++) {
    let c = s[i].charCodeAt();
    if (c >= 65 && c <= 90) {
      result += String.fromCharCode((c - 65 + 18) % 26 + 65);
    } else if (c >= 97 && c <= 122) {
      result += String.fromCharCode((c - 97 + 18) % 26 + 97);
    } else {
      result += s[i];
    }
  }
  return result;
}

