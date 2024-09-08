  let result = "";
  let consecutiveSpaces = 0;
  for (const c of text) {
    if (c == " ") {
      consecutiveSpaces += 1;
      if (consecutiveSpaces == 2) {
        result += "-";
        consecutiveSpaces = 1;
      } else {
        result += "_";
      }
    } else {
      result += c;
      consecutiveSpaces = 0;
    }
  }

  return result;
}



