  if (Object.keys(dict).length == 0) {
    return false;
  }
  let allLower = true;
  let allUpper = true;
  for (const key of Object.keys(dict)) {
    if (!allLower && !allUpper) {
      return false;
    }
    if (allLower) {
      allLower = allLower && key.toLowerCase() == key;
    }
    if (allUpper) {
      allUpper = allUpper && key.toUpperCase() == key;
    }
  }
  return allLower || allUpper;
}



