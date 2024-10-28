/*
  Given a string text, replace all spaces in it with underscores, 
  and if a string has more than 2 consecutive spaces, 
  then replace all consecutive spaces with - 
  
  fixSpaces("Example") == "Example"
  fixSpaces("Example 1") == "Example_1"
  fixSpaces(" Example 2") == "_Example_2"
  fixSpaces(" Example   3") == "_Example-3"
  */
const fixSpaces = (text) => {
  const underscoreSpace = '_';
  const hyphenSpace = '-';
  
  const textArray = text.split(' ');
  let result = '';

  for (let i = 0; i < textArray.length; i++) {
    const word = textArray[i];

    if (word.length > 2) {
      result += word.split('').join(hyphenSpace);
    } else {
      result += word.split('').join(underscoreSpace);
    }
  }

  return result;
}