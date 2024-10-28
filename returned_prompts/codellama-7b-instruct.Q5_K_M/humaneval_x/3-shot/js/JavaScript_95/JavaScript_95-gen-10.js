  if (len(dict) == 0) {
    return false;
  }

  for (const key of Object.keys(dict)) {
    if (typeof key != "string") {
      return false;
    }

    if (key.toLowerCase() != key && key.toUpperCase() != key) {
      return false;
    }
  }

  return true;
}



