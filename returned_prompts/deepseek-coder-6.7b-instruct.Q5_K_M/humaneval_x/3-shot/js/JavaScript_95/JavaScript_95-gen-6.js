  let isLower = true, isUpper = true;

  for (let key in dict) {
    if (key !== key.toLowerCase()) isLower = false;
    if (key !== key.toUpperCase()) isUpper = false;
  }

  return isLower || isUpper;
}



