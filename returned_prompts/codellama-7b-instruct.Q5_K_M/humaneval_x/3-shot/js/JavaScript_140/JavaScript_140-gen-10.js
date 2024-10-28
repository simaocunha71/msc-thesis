  let result = "";
  for (let c of text) {
    if (c == " ") {
      result += "_";
    } else {
      result += c;
    }
  }
  return result;
}



