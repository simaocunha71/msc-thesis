  if (Object.keys(dict).length === 0) {
    return false;
  }
  var allLower = true;
  var allUpper = true;
  for (const key of Object.keys(dict)) {
    if (!key.match(/^[a-z]+$/)) {
      allLower = false;
    }
    if (!key.match(/^[A-Z]+$/)) {
      allUpper = false;
    }
  }
  return allLower || allUpper;
}