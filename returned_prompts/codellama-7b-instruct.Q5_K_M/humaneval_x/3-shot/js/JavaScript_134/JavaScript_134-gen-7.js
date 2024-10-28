  const last_char = txt[txt.length - 1];
  const is_letter = (last_char.match(/[a-zA-Z]/) !== null);
  const is_word_char = (last_char.match(/\S/) !== null);
  return is_letter && !is_word_char;
}



