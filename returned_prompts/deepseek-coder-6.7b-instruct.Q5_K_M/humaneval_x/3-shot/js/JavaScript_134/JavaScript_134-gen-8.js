  let lastChar = txt.charAt(txt.length - 1);
  return lastChar.match(/[a-z]/i) && !txt.slice(0, -1).includes(lastChar);
}



