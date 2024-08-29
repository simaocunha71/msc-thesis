  let result = "";
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    result += String.fromCharCode(char.charCodeAt(0) + 1);
  }
  return result;
}



