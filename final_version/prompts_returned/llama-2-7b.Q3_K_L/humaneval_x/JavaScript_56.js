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
  let currentBracket = '';
  const isValidString = ({ type }) => {
    if (type !== 'opening' || !currentBracket.length) {
      return true;
    } else if (currentBracket === brackets[0]) {
      currentBracket = '';
    } else {
      console.log('not valid!', brackets);
    }
  };
  const isValid = ({ type }) => {
    if (type !== 'opening') return false;
    if (!currentBracket) return true;

    let valid = true;
    for (let i = 0; i < brackets.length; ++i) {
      if (brackets[i] === currentBracket) continue;
      valid &= isValidString({ type: 'closing' });
      break;
    }
    return valid;
  };
  for (let i = 0; i < brackets.length; ++i) {
    if (!isValidString({ type: 'opening', index: i }) && !isValid({ type: 'closing' })) {
      console.log('not valid!', brackets);
      break;
    }
  }
  return false;
};
