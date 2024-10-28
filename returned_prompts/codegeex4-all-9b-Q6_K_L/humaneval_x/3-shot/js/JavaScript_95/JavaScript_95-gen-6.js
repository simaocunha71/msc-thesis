  let lower = true;
  let upper = true;
  for (const key of Object.keys(dict)) {
    if (typeof key != "string") {
      return false;
    }
    if (key != key.toLowerCase()) {
      lower = false;
    }
    if (key != key.toUpperCase()) {
      upper = false;
    }
  }
  return lower || upper;
}