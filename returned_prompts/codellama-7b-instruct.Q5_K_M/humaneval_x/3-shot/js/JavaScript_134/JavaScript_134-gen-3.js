  const last_char = txt[txt.length - 1];
  if (last_char.match(/[a-zA-Z]/)) {
    if (txt.slice(-2, -1).match(/\s/)) {
      return true;
    }
  }
  return false;
}



