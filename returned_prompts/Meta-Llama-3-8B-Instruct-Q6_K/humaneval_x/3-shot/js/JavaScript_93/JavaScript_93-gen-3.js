  let result = '';
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char.match(/[a-z]/)) {
      char = char.toUpperCase();
    } else if (char.match(/[A-Z]/)) {
      char = char.toLowerCase();
    } else if (char.match(/[aeiouAEIOU]/)) {
      let index = 'abcdefghijklmnopqrstuvwxyz'.indexOf(char.toLowerCase());
      char = String.fromCharCode(index + 2);
    }
    result += char;
  }
  return result;
}



