  if (Object.keys(dict).length == 0) {
    return false;
  }
  var allLower = true;
  var allUpper = true;
  for (const key of Object.keys(dict)) {
    if (!Number.isInteger(key)) {
      if (key != key.toLowerCase()) {
        allLower = false;
      }
      if (key != key.toUpperCase()) {
        allUpper = false;
      }
    } else {
      allLower = false;
      allUpper = false;
    }
  }
  return allLower || allUpper;
}