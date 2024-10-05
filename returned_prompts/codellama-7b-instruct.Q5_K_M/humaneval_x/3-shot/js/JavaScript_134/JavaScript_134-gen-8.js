  const last_char = txt.slice(-1);
  if (last_char.match(/[a-zA-Z]/)) {
    if (last_char.match(/[a-z]/)) {
      if (last_char.match(/\s/)) {
        return false;
      } else {
        return true;
      }
    } else if (last_char.match(/[A-Z]/)) {
      if (last_char.match(/\s/)) {
        return false;
      } else {
        return true;
      }
    } else {
      return false;
    }
  } else {
    return false;
  }
}



