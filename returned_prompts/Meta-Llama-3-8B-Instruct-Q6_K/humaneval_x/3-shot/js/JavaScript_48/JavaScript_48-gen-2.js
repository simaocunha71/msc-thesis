  let reversed = '';
  for (let i = text.length - 1; i >= 0; i--) {
    reversed += text[i];
  }
  return text === reversed;
} // or return text.toLowerCase() === reversed.toLowerCase(); if you want to ignore case



