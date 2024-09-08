  const keys = Object.keys(dict);
  const values = Object.values(dict);

  for (let i = 0; i < keys.length; i++) {
    if (keys[i] != keys[i].toLowerCase() && keys[i] != keys[i].toUpperCase()) {
      return false;
    }
  }

  return true;
}



