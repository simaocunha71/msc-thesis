  if (Object.keys(dict).length == 0) {
    return false;
  }

  let allLower = true;
  let allUpper = true;

  for (const key in dict) {
    if (!allLower && !allUpper) {
      break;
    }
    if (allLower) {
      if (key[0].charCodeAt(0) >= 65) {
        allLower = false;
      }
    }
    if (allUpper) {
      if (key[0].charCodeAt(0) < 65) {
        allUpper = false;
      }
    }
  }

  return allLower || allUpper;
}