  if (Object.keys(dict).length === 0) {
    return false;
  }

  let allLower = true;
  let allUpper = true;

  for (const key in dict) {
    if (!(key === key.toLowerCase() || key === key.toUpperCase())) {
      return false;
    }
    if (!key.toLowerCase().equals(key)) {
      allLower = false;
    }
    if (!key.toUpperCase().equals(key)) {
      allUpper = false;
    }
  }

  return allLower || allUpper;
}
// checkDictCase({"STATE":"NC", "ZIP":"12345" }) returns true
// checkDictCase({"STATE":"NC", "Zip":"12345" }) returns false
// checkDictCase({"STATE":"NC", "zip":"12345" }) returns false
// checkDictCase({"STATE":"NC", "ziP":"12345" }) returns false
// checkDictCase({"STATE":"NC", "ZI P":"12345" }) returns false
// checkDictCase({"STATE":"NC", "12345":"12345" }) returns false
// checkDictCase({"STATE":"NC", "STATE":"NC" }) returns false
// checkDictCase({"STATE":"NC", "12345":"12345" }) returns false
// checkDictCase({"STATE":"NC", "STATE":"NC" }) returns false
// checkDictCase({"STATE":"NC", "12345":"12345" }) returns false
// checkDictCase({"STATE":"NC", "STATE":"NC" }) returns false
// checkDictCase({"STATE":"NC", "12345":"12345" }) returns false
// checkDictCase({"STATE":"NC", "STATE":"NC" }) returns false
// checkDictCase({"STATE":"NC", "12345":"12345" }) returns false
// checkDictCase({"STATE":"NC", "STATE":"NC" }) returns false
// checkDictCase({"STATE":"NC", "12345":"12345" }) returns false
// checkDictCase({"STATE":"NC", "STATE":"NC" }) returns false
// checkDictCase({"STATE":"NC", "12345":"12345" }) returns false
// checkDictCase({"STATE":"NC", "STATE":"NC" }) returns false
// checkDictCase({"STATE":"NC", "12345":"12345" }) returns false
// checkDictCase({"STATE":"NC", "STATE":"NC" }) returns false
