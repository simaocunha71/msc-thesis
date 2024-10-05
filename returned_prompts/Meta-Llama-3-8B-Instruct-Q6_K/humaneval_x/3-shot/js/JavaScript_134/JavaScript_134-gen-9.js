  let lastChar = txt.slice(-1);
  if (lastChar.match(/[a-zA-Z]/) && !/[a-zA-Z]/.test(txt.slice(0, -1))) {
    return true;
  }
  return false;
}