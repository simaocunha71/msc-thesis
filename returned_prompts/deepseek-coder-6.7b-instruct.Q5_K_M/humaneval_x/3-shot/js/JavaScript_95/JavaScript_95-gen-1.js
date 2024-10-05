  let lower_case_keys = Object.keys(dict).every(key => key === key.toLowerCase());
  let upper_case_keys = Object.keys(dict).every(key => key === key.toUpperCase());
  
  return lower_case_keys || upper_case_keys;
}



