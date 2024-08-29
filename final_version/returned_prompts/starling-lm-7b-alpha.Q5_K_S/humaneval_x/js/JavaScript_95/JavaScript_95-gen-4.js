  let upperCaseKeys = false;
  let lowerCaseKeys = false;
  for (const key in dict) {
    if (key.charAt(0).toLowerCase() != key.charAt(0)) {
      upperCaseKeys = true;
    } else if (key.charAt(0).toUpperCase() != key.charAt(0)) {
      lowerCaseKeys = true;
    }
  }
  return upperCaseKeys && lowerCaseKeys;
}



