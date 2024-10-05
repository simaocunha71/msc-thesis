  let result = '';
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char.match(/[a-zA-Z]/)) {
      let code = char.charCodeAt(0);
      if (char.match(/[aA]/)) {
        char = String.fromCharCode((code + 2) % 26 + 'a'.charCodeAt(0));
      } else if (char.match(/[eE]/)) {
        char = String.fromCharCode((code + 5) % 26 + 'e'.charCodeAt(0));
      } else if (char.match(/[iI]/)) {
        char = String.fromCharCode((code + 9) % 26 + 'i'.charCodeAt(0));
      } else if (char.match(/[oO]/)) {
        char = String.fromCharCode((code + 11) % 26 + 'o'.charCodeAt(0));
      } else if (char.match(/[uU]/)) {
        char = String.fromCharCode((code + 13) % 26 + 'u'.charCodeAt(0));
      } else if (char.match(/[yY]/)) {
        char = String.fromCharCode((code + 17) % 26 + 'y'.charCodeAt(0));
      } else {
        char = String.fromCharCode((code + 20) % 26 + 'a'.charCodeAt(0));
      }
      result += char.toUpperCase();
    } else {
      result += char;
    }
  }
  return result;
}



