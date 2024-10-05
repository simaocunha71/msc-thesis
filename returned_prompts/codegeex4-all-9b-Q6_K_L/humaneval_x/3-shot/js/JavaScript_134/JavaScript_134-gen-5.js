  if (txt == '') return false;
  let last_char = txt[txt.length - 1];
  if (last_char >= 'a' && last_char <= 'z') return true;
  if (last_char >= 'A' && last_char <= 'Z') return true;
  return false;
}



