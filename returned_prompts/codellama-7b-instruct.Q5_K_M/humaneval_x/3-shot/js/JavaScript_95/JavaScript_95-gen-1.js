  if (Object.keys(dict).length == 0) {
    return false;
  }

  var lower = [];
  var upper = [];

  for (key in dict) {
    if (typeof key == 'string') {
      lower.push(key.toLowerCase());
      upper.push(key.toUpperCase());
    }
  }

  if (lower.length == 0) {
    return false;
  }

  if (lower.length == Object.keys(dict).length) {
    return true;
  }

  if (upper.length == Object.keys(dict).length) {
    return true;
  }

  return false;
}



