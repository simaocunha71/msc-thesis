  let result = [];
  let char = txt.charAt(0);
  let count = 0;
  let index = 0;

  while (index < txt.length) {
    if (char == ' ') {
      result.push(txt.substring(index, index + 1));
      index++;
    } else if (char == ',') {
      result.push(txt.substring(index, index + 1));
      index++;
    } else if (char.match(/[a-zA-Z]/)) {
      let char_code = char.charCodeAt(0);
      if (char_code % 2 == 1) {
        count += 1;
      }
      index++;
    } else {
      index++;
    }
    char = txt.charAt(index);
  }

  if (result.length == 0) {
    return count;
  }

  return result;
}



