  if  (Object.keys(dict).length == 0) {
    return false;
  }

  let isLower = true;
  let isUpper = true;

  for  (let key in dict) {
    if  (key != key.toLowerCase()) {
      isLower = false;
    }
    if  (key != key.toUpperCase()) {
      isUpper = false;
    }
    if  (!isLower  &&  !isUpper) {
      break;
    }
  }

  return isLower  ||  isUpper;
}



