  if (Object.keys(dict).length === 0) {
    return false;
  }
  let allLower = true;
  let allUpper = true;
  for (const key in dict) {
    if (typeof key !== 'string') {
      return false;
    }
    if (!key.match(/^[a-z]+$/)) {
      allLower = false;
    }
    if (!key.match(/^[A-Z]+$/)) {
      allUpper = false;
    }
  }
  return allLower || allUpper;
}  // 10 points



