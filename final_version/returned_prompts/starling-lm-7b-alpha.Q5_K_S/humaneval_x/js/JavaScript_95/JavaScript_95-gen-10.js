  let allLowerCase = true;
  let allUpperCase = true;
  let dictLength = Object.keys(dict).length;
  for (let i = 0; i < dictLength; i++) {
    if (typeof dict[Object.keys(dict)[i]] === 'string') {
      if (Object.keys(dict)[i] === Object.keys(dict)[i].toLowerCase()) {
        allLowerCase = false;
      } else if (Object.keys(dict)[i] === Object.keys(dict)[i].toUpperCase()) {
        allUpperCase = false;
      }
    } else {
      return false;
    }
  }
  if (allLowerCase) {
    return true;
  } else if (allUpperCase) {
    return true;
  } else {
    return false;
  }
}



