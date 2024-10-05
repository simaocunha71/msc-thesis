  if (txt.length == 0) {
    return false;
  } else if (txt.length == 1) {
    if (txt.charCodeAt(0) >= 65 && txt.charCodeAt(0) <= 90) {
      return true;
    } else if (txt.charCodeAt(0) >= 97 && txt.charCodeAt(0) <= 122) {
      return true;
    } else {
      return false;
    }
  } else {
    let last_char = txt.charAt(txt.length - 1);
    let penult_char = txt.charAt(txt.length - 2);

    if (last_char.match(/[a-zA-Z]/)) {
      if (last_char == penult_char) {
        return false;
      } else {
        return true;
      }
    } else {
      return false;
    }
  }
}



