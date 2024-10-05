  if (Object.keys(dict).length == 0) return false;
  let keys = Object.keys(dict);
  let values = Object.values(dict);
  let key_case = keys.map(x => x.toLowerCase());
  let value_case = values.map(x => x.toLowerCase());

  return (key_case.every(x => typeof x === 'string') && value_case.every(x => typeof x === 'string')) ||
  (key_case.every(x => typeof x === 'string') && value_case.every(x => typeof x === 'string'));


}



