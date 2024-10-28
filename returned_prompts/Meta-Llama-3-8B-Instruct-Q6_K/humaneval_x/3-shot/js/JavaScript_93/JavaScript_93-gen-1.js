  let result = '';
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char.match(/[a-zA-Z]/)) {
      if (char.toUpperCase() === char) {
        char = char.toLowerCase();
      } else {
        char = char.toUpperCase();
      }
      if (char.match(/[aeiou]/i)) {
        let index = 'abcdefghijklmnopqrstuvwxyz'.indexOf(char.toLowerCase());
        index += 2;
        char = 'abcdefghijklmnopqrstuvwxyz'.charAt(index % 26);
      }
    }
    result += char;
  }
  return result;
}