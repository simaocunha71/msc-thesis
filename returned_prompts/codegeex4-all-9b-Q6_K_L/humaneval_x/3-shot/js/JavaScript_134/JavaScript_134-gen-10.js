  if (txt == "") return false;
  const last_char = txt[txt.length - 1];
  return /[a-zA-Z]/.test(last_char) && last_char != " ";
}



