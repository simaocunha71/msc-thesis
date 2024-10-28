  /*
  first convert the string to an array
  then count the number of "<" and ">"
  return false if the number of "<" is not equal to the number of ">"
  */
  const bracketArr = brackets.split('');
  const openBracketCount = bracketArr.filter(bracket => bracket === '<').length;
  const closeBracketCount = bracketArr.filter(bracket => bracket === '>').length;
  return (openBracketCount !== closeBracketCount) ? false : true;
};
