  let result = '';
  let message_array = message.split('');

  for (const c of message_array) {
    if (c.match(/[a-z]/)) {
      result += String.fromCharCode(
        c.charCodeAt(0) + 2 - 'a'.charCodeAt(0)
      );
    } else {
      result += c;
    }
  }

  return result;
}



