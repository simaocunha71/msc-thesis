  var result = "";
  var is_letter = false;
  for (const c of s) {
    if (c >= 'a' && c <= 'z') {
      result += String.fromCharCode(c.charCodeAt(0) - 32);
      is_letter = true;
    } else if (c >= 'A' && c <= 'Z') {
      result += String.fromCharCode(c.charCodeAt(0) + 32);
      is_letter = true;
    } else {
      result += c;
    }
  }

  return is_letter ? result : s.split('').reverse().join('');
}



