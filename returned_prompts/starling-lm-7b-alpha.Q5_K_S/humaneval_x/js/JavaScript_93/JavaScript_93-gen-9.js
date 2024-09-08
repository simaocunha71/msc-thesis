  let result = "";
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char == char.toLowerCase()) {
      char = char.toUpperCase();
    } else {
      char = char.toLowerCase();
    }
    if (['a', 'e', 'i', 'o', 'u'].includes(char)) {
      char = String.fromCharCode(char.charCodeAt(0) + 2);
    }
    result += char;
  }
  return result;
}



