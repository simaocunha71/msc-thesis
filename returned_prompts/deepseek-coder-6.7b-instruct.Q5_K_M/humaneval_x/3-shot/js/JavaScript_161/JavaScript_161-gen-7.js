  let result = '';
  for(let i = 0; i < s.length; i++) {
    if(s[i].match(/[a-zA-Z]/)) {
      result += s[i] === s[i].toLowerCase() ? s[i].toUpperCase() : s[i].toLowerCase();
    } else {
      result += s[i];
    }
  }
  return result;
}



