/* brackets is a string of "<" and ">".
  return false if every opening bracket has a corresponding closing bracket.

  >>> correctBracketing("<")
  false
  >>> correctBracketing("<>")
  false
  >>> correctBracketing("<<><>>")
  false
  >>> correctBracketing("><<>")
  false
  */
const correctBracketing = (brackets) => {
  const correctOpenings = brackets.split('').filter(char=>{
    return char === '<';
  });
  
  const correctClosers = brackets.split('').filter(char=>{
    return char === '>';
  });
  
  let count = brackets.length;

  while (count) {
    if (!correctOpenings[0] && !correctClosers[count -1]) {
      count--;
      continue;
    } else if (correctOpenings[0] && correctClosers[count -1]){
      break;
    }
    
  }
  
  return count ? true : false;
}
