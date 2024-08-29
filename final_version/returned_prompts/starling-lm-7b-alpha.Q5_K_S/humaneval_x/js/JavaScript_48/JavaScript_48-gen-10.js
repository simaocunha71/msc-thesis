  let reversed_text = '';
  for (let i = text.length - 1; i >= 0; i--) {
    reversed_text += text[i];
  }
  return text === reversed_text;
}



