  let encrypted = '';
  let shift = 2 * 2;
  for (let i = 0; i < s.length; i++) {
    let c = s.charCodeAt(i);
    if (c >= 65 && c <= 90) { // uppercase letter
      c = (c - 65 + shift) % 26 + 65;
    } else if (c >= 97 && c <= 122) { // lowercase letter
      c = (c - 97 + shift) % 26 + 97;
    } else {
      encrypted += String.fromCharCode(c);
    }
    encrypted += String.fromCharCode(c);
  }
  return encrypted;
} 