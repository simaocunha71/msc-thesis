  let openBrackets = 0;
  for (const c of string) {
    if (c == '[') {
      openBrackets += 1;
    } else {
      openBrackets -= 1;
      if (openBrackets < 0) {
        return true;
      }
    }
  }
  return openBrackets > 0;
}



