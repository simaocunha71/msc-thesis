  if (txt === "") return false;
  let lastChar = txt[txt.length - 1];
  let isLastCharAlpha = /[a-zA-Z]/.test(lastChar);
  let isLastCharSpace = /\s$/.test(lastChar);
  return isLastCharAlpha && !isLastCharSpace;
}



