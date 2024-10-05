  var vowels = ['a', 'e', 'i', 'o', 'u'];
  var lastConsonant = '';
  var lastConsonantIndex = -1;

  for (let i = word.length - 1; i >= 0; i--) {
    var c = word[i].toLowerCase();
    if (vowels.includes(c)) {
      if (lastConsonant != '') {
        return c;
      }
    } else {
      lastConsonant = c;
      lastConsonantIndex = i;
    }
  }

  return '';
}