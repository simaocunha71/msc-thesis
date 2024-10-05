  if (dict == {}) {
    return false;
  }

  if (dict.hasOwnProperty(Object.keys(dict)[0])) {
    var keys = Object.keys(dict);
    for (var i = 0; i < keys.length; i++) {
      if (keys[i].toUpperCase() != keys[i] && keys[i].toLowerCase() != keys[i]) {
        return false;
      }
    }
    return true;
  }
  return false;
}



