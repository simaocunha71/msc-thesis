  let upper_case_key = false;
  let lower_case_key = false;
  for (const key in dict) {
    if (key.charAt(0).toUpperCase() == key.charAt(0) && key != key.toLowerCase()) {
      upper_case_key = true;
    } else if (key.charAt(0).toLowerCase() == key.charAt(0)) {
      lower_case_key = true;
    }
  }
  return !upper_case_key && lower_case_key;
}



