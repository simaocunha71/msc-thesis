  if (dict == {}) return false;
  let lower = 0;
  let upper = 0;
  for (const key in dict) {
    if (typeof(key) == 'string') {
      if (key == key.toLowerCase()) {
        lower += 1;
      } else if (key == key.toUpperCase()) {
        upper += 1;
      }
    }
  }
  return (lower == Object.keys(dict).length) | (upper == Object.keys(dict).length);
}



