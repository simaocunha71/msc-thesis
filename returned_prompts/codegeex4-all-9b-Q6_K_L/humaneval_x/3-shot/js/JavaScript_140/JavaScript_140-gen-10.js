  var result = "";

  for (const c of text) {
    if (c == " ") {
      if (result.slice(-1) == " ") {
        result += "-";
      } else {
        result += "_";
      }
    } else {
      result += c;
    }
  }

  return result;
}