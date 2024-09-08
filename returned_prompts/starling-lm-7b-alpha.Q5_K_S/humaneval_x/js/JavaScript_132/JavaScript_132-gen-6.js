  const openBrackets = new Set(['[', '(', '{']);
  const closeBrackets = new Set([']', ')', '}']);
  const openingBracket = new Set(openBrackets).add(string[0]);
  const closingBracket = closeBrackets.add(string[string.length - 1]);

  if (openingBracket.size === 1 && closingBracket.size === 1) {
    return true;
  }

  return false;
}



