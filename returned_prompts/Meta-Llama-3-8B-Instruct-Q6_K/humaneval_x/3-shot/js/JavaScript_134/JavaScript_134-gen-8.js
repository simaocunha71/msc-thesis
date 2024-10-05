  if (txt.length == 0) {
    return false;
  }
  let last_char = txt[txt.length - 1];
  if (!/[a-zA-Z]/.test(last_char)) {
    return false;
  }
  if (txt[txt.length - 2] != ' ' && txt[txt.length - 3] != ' ') {
    return true;
  }
  return false;
}