  let all_upper = true;
  let all_lower = true;

  for (const key of Object.keys(dict)) {
    if (typeof(key) != 'string') {
      return false;
    }
    if (key != key.toUpperCase()) {
      all_upper = false;
    }
    if (key != key.toLowerCase()) {
      all_lower = false;
    }
  }

  return all_lower || all_upper;
}



