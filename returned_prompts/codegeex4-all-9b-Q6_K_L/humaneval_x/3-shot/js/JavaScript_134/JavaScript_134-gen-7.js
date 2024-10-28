  var last_char = txt[txt.length - 1];
  var is_letter = (last_char >= 'a' && last_char <= 'z') || (last_char >= 'A' && last_char <= 'Z');
  var is_not_word = txt[txt.length - 2] == ' ';
  return is_letter && is_not_word;
}