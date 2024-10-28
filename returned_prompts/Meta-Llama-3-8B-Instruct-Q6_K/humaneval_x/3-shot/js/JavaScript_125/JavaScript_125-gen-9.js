  let words = txt.split(' ');
  if (!words.length) {
    words = txt.split(',');
  }
  if (!words.length) {
    return txt.toLowerCase().split('').filter((c, i) => (c >= 'a' && c <= 'z') && i % 2 !== 0).length;
  }
  return words;
}