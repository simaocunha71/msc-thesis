  let result = '';

  for (let i = 0; i < s.length; i++) {
    if (s[i].match(/[a-zA-Z]/)) {
      result += s[i].toUpperCase();
    } else {
      result += s[i];
    }
  }

  return result;
}



