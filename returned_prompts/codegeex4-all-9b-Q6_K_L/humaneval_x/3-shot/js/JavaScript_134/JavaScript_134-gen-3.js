  var last_char = txt[txt.length - 1];
  var last_is_letter = (last_char >= 'a' && last_char <= 'z') || (last_char >= 'A' && last_char <= 'Z');
  var last_is_not_word = txt[txt.length - 2] == ' ';
  return last_is_letter && last_is_not_word;
}