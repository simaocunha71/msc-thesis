  let result = '';
  for (let i = 0; i < s.length; i++) {
    if (/[a-zA-Z]/.test(s[i])) {
      result += s[i].toUpperCase() === s[i] ? s[i].toLowerCase() : s[i].toUpperCase();
    } else {
      result += s[i];
    }
  }
  return result.split('').reverse().join('');
}