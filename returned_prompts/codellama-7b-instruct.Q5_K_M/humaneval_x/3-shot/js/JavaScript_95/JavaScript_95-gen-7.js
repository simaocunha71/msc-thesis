  if (dict == {}) {
    return false;
  }
  for (const key in dict) {
    if (typeof(key) !== 'string') {
      return false;
    }
    if (key != key.toLowerCase() && key != key.toUpperCase()) {
      return false;
    }
  }
  return true;
}



