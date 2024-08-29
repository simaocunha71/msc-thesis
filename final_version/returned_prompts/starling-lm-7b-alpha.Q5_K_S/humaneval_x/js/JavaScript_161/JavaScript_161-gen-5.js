  let result = "";
  let hasLetter = false;
  for (const c of s) {
    if (c >= 'a' && c <= 'z') {
      result += String.fromCharCode(c - 32);
      hasLetter = true;
    } else if (c >= 'A' && c <= 'Z') {
      result += String.fromCharCode(c + 32);
      hasLetter = true;
    } else {
      result += c;
    }
  }

  if (!hasLetter) {
    result = s.split('').reverse().join('');
  }

  return result;
}



