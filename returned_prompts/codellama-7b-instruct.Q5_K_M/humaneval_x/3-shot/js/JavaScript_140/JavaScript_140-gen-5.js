  var result = "";
  for (let i = 0; i < text.length; i++) {
    if (text[i] == " ") {
      if (i < text.length - 1 && text[i + 1] == " ") {
        result += "-";
        i += 1;
      } else {
        result += "_";
      }
    } else {
      result += text[i];
    }
  }
  return result;
}



