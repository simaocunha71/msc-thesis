  let result = '';
  for (let char of message) {
    if (char.match(/[a-z]/i)) {
      if (char.toLowerCase() === 'a' || char.toLowerCase() === 'e' || char.toLowerCase() === 'i' || char.toLowerCase() === 'o' || char.toLowerCase() === 'u') {
        result += String.fromCharCode((char.charCodeAt(0) + 2) % 26 + 97);
      } else {
        result += char.toUpperCase();
      }
    } else {
      result += char;
    }
  }
  return result;
}