  let result = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] >= 'a' && s[i] <= 'z') {
      result += s[i].toUpperCase();
    } else if (s[i] >= 'A' && s[i] <= 'Z') {
      result += s[i].toLowerCase();
    } else {
      result += s[i];
    }
  }

  if (result.match(/[a-zA-Z]/g)) {
    return result;
  } else {
    return result.split('').reverse().join('');
  }
}