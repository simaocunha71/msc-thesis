  let result = '';

  for (let i = 0; i < message.length; i++) {
    if (message[i] === message[i].toLowerCase()) {
      result += String.fromCharCode(
        message.charCodeAt(i) + (message.charCodeAt(i) - 97 + 1) % 26 + 97);
    } else {
      result += String.fromCharCode(
        message.charCodeAt(i) + (message.charCodeAt(i) - 65 + 1) % 26 + 65);
    }
  }
  return result;
}



