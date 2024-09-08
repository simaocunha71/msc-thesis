  let result = '';

  for (let i = 0; i < s.length; i++) {
    if (s[i] >= 'a' && s[i] <= 'z') {
      result += String.fromCharCode(s[i] - 32);
    } else if (s[i] >= 'A' && s[i] <= 'Z') {
      result += String.fromCharCode(s[i] + 32);
    } else {
      result += s[i];
    }
  }

  return result;
}



