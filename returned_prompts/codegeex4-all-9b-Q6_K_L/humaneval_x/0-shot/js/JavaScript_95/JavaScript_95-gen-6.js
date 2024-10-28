const checkDictCase = (dict) => {
  if (!Object.keys(dict).length) return false;
  const isLowerCase = Object.keys(dict).every(key => key === key.toLowerCase());
  const isUpperCase = Object.keys(dict).every(key => key === key.toUpperCase());
  return isLowerCase || isUpperCase;
}