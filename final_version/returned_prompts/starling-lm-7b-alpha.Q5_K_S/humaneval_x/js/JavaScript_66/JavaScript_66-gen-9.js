  let result = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i].toUpperCase()) {
      result += s[i].charCodeAt();
    }
  }
  return result;
}



