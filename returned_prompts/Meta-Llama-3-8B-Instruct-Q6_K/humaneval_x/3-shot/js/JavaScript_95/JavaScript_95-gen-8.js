  if (Object.keys(dict).length === 0) {
    return false;
  }
  let allLower = true;
  let allUpper = true;

  for (const key in dict) {
    if (typeof key !== 'string') {
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
} // end function checkDictCase

// Helper function to convert a string to lower case.
String.prototype.equals = function(s) {
  return this === s;
}
String.prototype.toLowerCase = function() {
  return this;
}
String.prototype.toUpperCase = function() {
  return this;
} // end Helper function
} // end checkDictCase
} // end checkDictCase



