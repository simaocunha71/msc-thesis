  var result = '';
  var is_letter = false;

  for (const c of s) {
    if (is_letter) {
      if (c.toUpperCase() == c) {
        result += c.toLowerCase();
      } else {
        result += c.toUpperCase();
      }
      is_letter = false;
    } else {
      if (c.toLowerCase() == c) {
        result += c.toUpperCase();
      } else {
        result += c.toLowerCase();
      }
    }

    if (c.toLowerCase() == c || c.toUpperCase() == c) {
      is_letter = true;
    }
  }

  return result;
}



