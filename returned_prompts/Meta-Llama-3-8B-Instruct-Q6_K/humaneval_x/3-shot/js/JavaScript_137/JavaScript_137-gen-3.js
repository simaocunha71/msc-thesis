  if (typeof a === 'string' && typeof b === 'string') {
    a = parseFloat(a.replace(/,/g, ''));
    b = parseFloat(b.replace(/,/g, ''));
  }
  if (typeof a === 'number' && typeof b === 'number') {
    if (a === b) {
      return null;
    } else if (a > b) {
      return a;
    } else {
      return b;
    }
  }
  if (typeof a === 'string' && typeof b === 'number') {
    if (a === b.toString()) {
      return null;
    } else if (a > b.toString()) {
      return a;
    } else {
      return b.toString();
    }
  }
  if (typeof a === 'number' && typeof b === 'string') {
    if (a.toString() === b) {
      return null;
    } else if (a.toString() > b) {
      return a.toString();
    } else {
      return b;
    }
  }
}
// You can also use a simple function to compare two numbers
function compareNumbers(a, b) {
  if (a > b) {
    return a;
  } else if (a < b) {
    return b;
  } else {
    return null;
  }
}  // Used in the main function
// Used in the main function
function compareStrings(a, b) {
  if (a > b) {
    return a;
  } else if (a < b) {
    return b;
  } else {
    return null;
  }
}  // Used in the main function
// Used in the main function
function compare(a, b) {
  if (typeof a === 'number' && typeof b === 'number') {
    return compareNumbers(a, b);
  } else if (typeof a === 'string' && typeof b === 'string') {
    return compareStrings(a, b);
  } else {
    return null;
  }
}  // Used in the main function
// Used in the main function
function replaceComma(a) {
  return a.replace(/,/g, '');
}  // Used in the main function
// Used in the main function
function parseFloatWithComma(a) {
  return parseFloat(a.replace(/,/g, ''));
}  // Used in the main function
// Used in the main function
function compareOne(a, b) {
  if