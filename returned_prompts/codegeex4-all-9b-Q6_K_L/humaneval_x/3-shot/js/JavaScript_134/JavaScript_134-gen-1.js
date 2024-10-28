  const last_char = txt[txt.length - 1];
  const is_letter = last_char.match(/[a-zA-Z]/);
  if (is_letter) {
    const last_word = txt.split(" ").pop();
    const is_word = last_word.length == txt.length;
    return !is_word;
  }
  return false;
}