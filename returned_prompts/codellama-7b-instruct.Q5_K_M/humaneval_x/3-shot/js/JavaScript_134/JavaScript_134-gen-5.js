  if (txt.length === 0) {
    return false;
  }

  const last_char = txt[txt.length - 1];
  const before_last_char = txt[txt.length - 2];

  if (last_char.match(/\w$/)) {
    if (before_last_char === ' ') {
      return true;
    }
  }

  return false;
}



