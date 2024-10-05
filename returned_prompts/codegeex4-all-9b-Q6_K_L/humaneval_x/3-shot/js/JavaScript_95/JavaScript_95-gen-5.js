  if (Object.keys(dict).length === 0) {
    return false;
  } else {
    let first_key = Object.keys(dict)[0];
    if (first_key == first_key.toLowerCase()) {
      for (let key of Object.keys(dict)) {
        if (key != key.toLowerCase()) {
          return false;
        }
      }
      return true;
    } else if (first_key == first_key.toUpperCase()) {
      for (let key of Object.keys(dict)) {
        if (key != key.toUpperCase()) {
          return false;
        }
      }
      return true;
    } else {
      return false;
    }
  }
}



