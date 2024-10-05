const encrypt = (s) => {
  let newS = '';
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    let newChar = String.fromCharCode((char.charCodeAt() + 2 * 2) % 26 + 65);
    newS += newChar;
  }
  return newS;
};

