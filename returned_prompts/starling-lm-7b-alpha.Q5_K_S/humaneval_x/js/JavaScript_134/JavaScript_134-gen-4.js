  if (txt.length === 0) {
    return false;
  }

  let lastChar = txt[txt.length - 1];

  if (!/[a-zA-Z]/.test(lastChar)) {
    return false;
  }

  let currentIndex = txt.length - 1;
  let index = currentIndex;
  let isLastCharALetter = true;

  while (index >= 0) {
    if (!/[a-zA-Z]/.test(txt[index])) {
      isLastCharALetter = false;
      break;
    }
    if (txt[index] === ' ') {
      break;
    }
    index--;
  }

  return isLastCharALetter;
}



