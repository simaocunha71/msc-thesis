  if (Object.keys(dict).length == 0) {
    return false;
  }

  let all_lower = true;
  let all_upper = true;

  for (const key of Object.keys(dict)) {
    if (key != key.toLowerCase()) {
      all_lower = false;
    }
    if (key != key.toUpperCase()) {
      all_upper = false;
    }
  }

  return all_lower || all_upper;
}