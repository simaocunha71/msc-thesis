  if (dict == {}) {
    return false;
  }

  let keys = Object.keys(dict);
  let values = Object.values(dict);

  let key_case_type = keys[0].toLowerCase();
  let key_case_type2 = keys[0].toUpperCase();
  let value_case_type = values[0].toLowerCase();
  let value_case_type2 = values[0].toUpperCase();

  for (let key in keys) {
    if (keys[key].toLowerCase() != key_case_type) {
      if (keys[key].toUpperCase() != key_case_type2) {
        return false;
      }
    }
  }

  for (let value in values) {
    if (values[value].toLowerCase() != value_case_type) {
      if (values[value].toUpperCase() != value_case_type2) {
        return false;
      }
    }
  }

  return true;
}



