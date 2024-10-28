const correctBracketing = (brackets) => {
  // if the length of the brackets is odd, return false
  if (brackets.length % 2 !== 0) return false;

  // create an object to store opening brackets
  const openingBrackets = {
    "(": true,
    "{": true,
    "[": true
  };

  // create an object to store closing brackets
  const closingBrackets = {
    ")": true,
    "}": true,
    "]": true
  };

  // iterate through the string
  for (let i = 0; i < brackets.length; i++) {
    // if the current character is an opening bracket
    if (openingBrackets[brackets[i]]) {
      // add the corresponding closing bracket to the end of the string
      brackets += closingBrackets[brackets[i]];
    } else {
      // if the current character is a closing bracket
      // remove the corresponding opening bracket from the end of the string
      brackets = brackets.slice(0, -1);
    }
  }

  // if the string is empty, return true
  if (brackets === "") return true;

  // otherwise return false
  return false;
};

/*
