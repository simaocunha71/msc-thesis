  if (txt.length == 0) {
    return false;
  } else {
    let last_char = txt[txt.length - 1];
    if (last_char.match(/[a-z]/i) && !last_char.match(/[a-z][a-z]/i)) {
      return true;
    } else {
      return false;
    }
  }
}