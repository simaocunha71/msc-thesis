  let result = "";
  let consecutive_spaces = false;
  for (const c of text) {
    if (c == " ") {
      if (consecutive_spaces) {
        result += "-";
        consecutive_spaces = false;
      } else {
        result += "_";
        consecutive_spaces = true;
      }
    } else {
      result += c;
      consecutive_spaces = false;
    }
  }
  return result;
}



