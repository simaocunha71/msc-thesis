  if (txt.length === 0) return false;
  let lastChar = txt[txt.length - 1];
  if (!lastChar.match(/[a-z]/i)) return false;
  if (txt.match(/\w+\W+$/i)) return true;
  return false;
}

