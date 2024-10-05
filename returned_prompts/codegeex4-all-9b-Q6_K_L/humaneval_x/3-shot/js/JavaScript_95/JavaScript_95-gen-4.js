  if (Object.keys(dict).length == 0) return false;
  var first_key = Object.keys(dict)[0];
  if (first_key == first_key.toUpperCase()) {
    for (const key of Object.keys(dict)) {
      if (key != key.toUpperCase()) return false;
    }
  } else if (first_key == first_key.toLowerCase()) {
    for (const key of Object.keys(dict)) {
      if (key != key.toLowerCase()) return false;
    }
  } else {
    return false;
  }
  return true;
}