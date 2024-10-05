  if (dict === {}) return false;

  let keys = Object.keys(dict);
  for (let key of keys) {
    if (typeof key !== 'string') return false;
    if (key === key.toLowerCase()) continue;
    if (key === key.toUpperCase()) continue;
    return false;
  }

  return true;
}



