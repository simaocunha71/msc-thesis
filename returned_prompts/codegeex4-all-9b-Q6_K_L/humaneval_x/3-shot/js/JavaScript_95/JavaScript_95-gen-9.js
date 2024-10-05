  if (Object.keys(dict).length == 0) {
    return false;
  }

  for (const key of Object.keys(dict)) {
    if (typeof key !== 'string') {
      return false;
    }
    if (key !== key.toLowerCase() && key !== key.toUpperCase()) {
      return false;
    }
  }

  return true;
}