  const lastChar = txt.charAt(txt.length - 1);
  const secondToLastChar = txt.charAt(txt.length - 2);
  return /[a-zA-Z]/.test(lastChar) && secondToLastChar === ' ';
}



