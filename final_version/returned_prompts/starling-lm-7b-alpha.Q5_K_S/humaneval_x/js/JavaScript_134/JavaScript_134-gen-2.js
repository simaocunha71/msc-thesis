  if (txt.length == 0) {
    return false;
  }

  let lastChar = txt[txt.length - 1];
  if (!lastChar.match(/[a-zA-Z]/)) {
    return false;
  }

  let previousChar = txt[txt.length - 2];
  if (previousChar.match(/[a-zA-Z]/)) {
    return false;
  }

  return true;
}



