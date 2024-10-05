  let openBrackets = 0;
  let closeBrackets = 0;

  for (const c of brackets) {
    if (c == '<') {
      openBrackets++;
    } else if (c == '>') {
      closeBrackets++;
    }
  }

  return openBrackets == closeBrackets;
}