  let lastChar = txt.charAt(txt.length - 1);
  return /[a-z]/i.test(lastChar) && txt.substr(-2, 1) === " ";
}



