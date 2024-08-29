  const keys = Object.keys(dict);
  const lowerCaseKeys = keys.filter(key => typeof key === 'string' && key.toLowerCase() !== key);
  const upperCaseKeys = keys.filter(key => typeof key === 'string' && key.toUpperCase() !== key);
  return lowerCaseKeys.length === 0 && upperCaseKeys.length === 0;
}



