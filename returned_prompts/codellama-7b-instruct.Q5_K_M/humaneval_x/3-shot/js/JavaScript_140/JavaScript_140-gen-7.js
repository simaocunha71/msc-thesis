  let result = '';
  for (let i = 0; i < text.length; i++) {
    if (text[i] == ' ') {
      if (text[i + 1] == ' ' && text[i + 2] == ' ') {
        result += '-';
        i += 2;
      } else {
        result += '_';
      }
    } else {
      result += text[i];
    }
  }
  return result;
}



