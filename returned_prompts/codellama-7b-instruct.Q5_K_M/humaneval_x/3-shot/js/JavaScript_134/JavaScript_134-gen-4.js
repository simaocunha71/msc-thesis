  if (txt.length == 0)
    return false;
  else {
    var last_char = txt[txt.length - 1];
    var is_letter = last_char.match(/[a-zA-Z]/);
    if (is_letter != null) {
      var last_char_is_not_part_of_word = (txt.lastIndexOf(last_char) == txt.length - 1);
      if (last_char_is_not_part_of_word)
        return true;
      else
        return false;
    }
    else
      return false;
  }
}



