  let newStr = '';

  for (let i = 0; i < s.length; i++) {
    let char = s.charAt(i);
    if (char.match(/[a-z]/i)) {
      newStr += String.fromCharCode((char.charCodeAt() + 2 * 2 - 97) % 26 + 97);
    } else {
      newStr += char;
    }
  }

  return newStr;
}



