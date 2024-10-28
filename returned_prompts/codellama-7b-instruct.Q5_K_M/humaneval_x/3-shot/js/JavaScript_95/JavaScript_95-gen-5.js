  if (Object.keys(dict).length == 0)
    return false;

  let all_lower = true;
  let all_upper = true;

  for (let [key, value] of Object.entries(dict)) {
    if (typeof key !== 'string')
      return false;
    if (key !== key.toLowerCase() && key !== key.toUpperCase())
      all_lower = false;
    if (key !== key.toUpperCase() && key !== key.toLowerCase())
      all_upper = false;
    if (!all_lower && !all_upper)
      return false;
  }

  return all_lower || all_upper;
}



