  if (txt.length == 0) {
    return false;
  }
  if (!txt.match(/[a-zA-Z]/)) {
    return false;
  }
  if (txt[txt.length - 1].match(/[\s]+/)) {
    return false;
  }
  return true;
}



