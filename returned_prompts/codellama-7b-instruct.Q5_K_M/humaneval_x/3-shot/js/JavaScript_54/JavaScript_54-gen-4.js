  var char_dict = {};

  for (const c of s0) {
    if (!char_dict.hasOwnProperty(c)) {
      char_dict[c] = 1;
    } else {
      char_dict[c] += 1;
    }
  }

  for (const c of s1) {
    if (!char_dict.hasOwnProperty(c)) {
      return false;
    }
    char_dict[c] -= 1;
    if (char_dict[c] == 0) {
      delete char_dict[c];
    }
  }

  for (const c in char_dict) {
    if (char_dict[c] != 0) {
      return false;
    }
  }

  return true;
}



