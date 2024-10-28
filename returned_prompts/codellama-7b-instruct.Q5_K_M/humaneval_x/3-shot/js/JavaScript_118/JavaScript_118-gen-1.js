  const vowels = ['a', 'e', 'i', 'o', 'u'];
  const consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'];
  const word_length = word.length;

  var closest_vowel = '';
  for (let i = 0; i < word_length; i++) {
    var char = word[i];
    if (vowels.includes(char)) {
      closest_vowel = char;
      break;
    }
  }

  for (let i = word_length - 1; i >= 0; i--) {
    var char = word[i];
    if (vowels.includes(char)) {
      if (char != closest_vowel) {
        return char;
      } else {
        break;
      }
    }
  }

  return '';
}



