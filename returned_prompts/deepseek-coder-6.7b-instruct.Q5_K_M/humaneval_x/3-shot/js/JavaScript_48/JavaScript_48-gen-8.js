  const len = text.length;
  for  (let i = 0; i < len/2; i++) {
    if  (text[i] !== text[len - 1 - i]) {
      return false;
    }
  }
  return true;
}



