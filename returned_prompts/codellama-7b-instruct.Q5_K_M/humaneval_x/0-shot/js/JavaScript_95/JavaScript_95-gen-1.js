  const allLowerCase = (str) => str === str.toLowerCase();
  const allUpperCase = (str) => str === str.toUpperCase();

  if(Object.keys(dict).length === 0) return false;

  const keys = Object.keys(dict);

  if(keys.every(allLowerCase) || keys.every(allUpperCase)) return true;

  return false;

