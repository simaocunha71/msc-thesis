  if (Object.keys(dict).length === 0) {
    return false;
  }
  var firstKey = Object.keys(dict)[0];
  if (firstKey === firstKey.toLowerCase()) {
    for (const key of Object.keys(dict)) {
      if (key !== key.toLowerCase()) {
        return false;
      }
    }
  } else if (firstKey === firstKey.toUpperCase()) {
    for (const key of Object.keys(dict)) {
      if (key !== key.toUpperCase()) {
        return false;
      }
    }
  } else {
    return false;
  }
  return true;
}



