  const last_char = txt[txt.length - 1];
  const last_char_is_letter = last_char.toLowerCase() >= 'a' && last_char.toLowerCase() <= 'z';
  const last_char_is_part_of_word = txt.split(' ').pop().length > 1;
  return last_char_is_letter && !last_char_is_part_of_word;
}



