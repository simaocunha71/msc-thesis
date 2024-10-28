  let lastChar = txt.slice(-1);
  let lastWord = txt.split(' ').pop();
  return /^[a-zA-Z]$/.test(lastChar) && !lastWord.includes(lastChar);
}