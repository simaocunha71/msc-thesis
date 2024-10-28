  const lastChar = txt[txt.length - 1];
  return /[a-z]/i.test(lastChar) && txt[txt.length - 2] === " ";
}



