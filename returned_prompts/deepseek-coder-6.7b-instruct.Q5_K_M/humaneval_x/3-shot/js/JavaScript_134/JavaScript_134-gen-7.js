  let lastChar = txt[txt.length - 1];
  let secondToLastChar = txt[txt.length - 2];
  return /[a-zA-Z]/.test(lastChar) && secondToLastChar === ' ' || txt.length === 0;
}



