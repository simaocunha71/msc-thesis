  if (txt === "") {
    return false;
  }

  let index = txt.length - 1;
  while (index >= 0 && !txt[index].match(/[a-zA-Z]/)) {
    index -= 1;
  }

  return index >= 0 && txt[index].match(/[a-zA-Z]/);
}



