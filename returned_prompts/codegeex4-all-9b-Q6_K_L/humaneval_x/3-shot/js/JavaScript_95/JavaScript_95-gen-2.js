  if (Object.keys(dict).length == 0) {
    return false;
  }
  let first_key = Object.keys(dict)[0];
  if (first_key.toUpperCase() == first_key) {
    for (const key of Object.keys(dict)) {
      if (key.toUpperCase() != key) {
        return false;
      }
    }
    return true;
  } else if (first_key.toLowerCase() == first_key) {
    for (const key of Object.keys(dict)) {
      if (key.toLowerCase() != key) {
        return false;
      }
    }
    return true;
  } else {
    return false;
  }
}