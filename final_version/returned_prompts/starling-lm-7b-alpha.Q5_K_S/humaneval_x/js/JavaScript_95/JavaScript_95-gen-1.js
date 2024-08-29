  if (Object.keys(dict).length === 0) {
    return false;
  }

  let keys = Object.keys(dict);
  for (let key of keys) {
    if (key.toLowerCase() !== key || key.toUpperCase() !== key) {
      return false;
    }
  }
  return true;
}



