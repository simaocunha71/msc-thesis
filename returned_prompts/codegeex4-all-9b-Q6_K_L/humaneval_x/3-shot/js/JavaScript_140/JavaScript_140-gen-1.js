  let result = "";
  let space_count = 0;

  for (const c of text) {
    if (c == " ") {
      space_count += 1;
    } else {
      if (space_count == 1) {
        result += "_";
      } else if (space_count == 2) {
        result += "-";
      } else if (space_count > 2) {
        result += "-";
      }
      result += c;
      space_count = 0;
    }
  }
  return result;
}