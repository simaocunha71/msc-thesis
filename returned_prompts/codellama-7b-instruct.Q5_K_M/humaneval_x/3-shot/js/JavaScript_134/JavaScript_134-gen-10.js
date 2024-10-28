  if (txt.length < 1)
    return false;

  var last_char = txt.charAt(txt.length - 1);
  var last_char_is_letter = (last_char >= 'a' && last_char <= 'z') || (last_char >= 'A' && last_char <= 'Z');

  if (last_char_is_letter) {
    var last_word = txt.substr(0, txt.length - 1);
    var last_word_has_space = last_word.charAt(last_word.length - 1) == ' ';
    if (last_word_has_space)
      return false;
    else
      return true;
  }
  else
    return false;
}



