  var result = '';
  for(let i = 0; i < message.length; i++) {
    let char = message[i];
    if(/[a-z]/.test(char)) {
      if(/[aeiou]/.test(char)) {
        result += String.fromCharCode(char.charCodeAt(0) + 2);
      } else {
        result += char.toUpperCase();
      }
    } else if(/[A-Z]/.test(char)) {
      if(/[AEIOU]/.test(char)) {
        result += String.fromCharCode(char.charCodeAt(0) + 2);
      } else {
        result += char.toLowerCase();
      }
    } else {
      result += char;
    }
  }
  return result;
}



