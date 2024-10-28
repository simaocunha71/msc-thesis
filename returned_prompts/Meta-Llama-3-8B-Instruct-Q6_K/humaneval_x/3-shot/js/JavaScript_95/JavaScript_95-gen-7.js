  if (Object.keys(dict).length === 0) {
    return false;
  }

  let allLower = true;
  let allUpper = true;

  for (const key of Object.keys(dict)) {
    if (!key.match(/^[a-z]+$/)) {
      allLower = false;
    }
    if (!key.match(/^[A-Z]+$/)) {
      allUpper = false;
    }
    if (!allLower && !allUpper) {
      return false;
    }
  }

  return allLower || allUpper;
}