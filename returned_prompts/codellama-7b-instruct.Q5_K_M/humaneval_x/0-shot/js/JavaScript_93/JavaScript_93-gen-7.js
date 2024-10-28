const encode = (message) => {
  let encoded = '';
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char.match(/[a-z]/)) {
      char = char.toUpperCase();
    } else if (char.match(/[A-Z]/)) {
      char = char.toLowerCase();
    }
    if (char.match(/[a-zA-Z]/)) {
      let index = char.charCodeAt(0) + 2;
      if (index > 90) {
        index -= 26;
      }
      char = String.fromCharCode(index);
    }
    encoded += char;
  }
  return encoded;
};
