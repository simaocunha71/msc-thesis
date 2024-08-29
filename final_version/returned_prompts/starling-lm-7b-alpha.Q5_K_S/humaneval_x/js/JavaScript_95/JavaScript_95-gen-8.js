  const keys = Object.keys(dict);
  for (let key of keys) {
    if (typeof(key) != 'string' || (key != key.toLowerCase() && key != key.toUpperCase())) {
      return false;
    }
  }
  return true;
}



