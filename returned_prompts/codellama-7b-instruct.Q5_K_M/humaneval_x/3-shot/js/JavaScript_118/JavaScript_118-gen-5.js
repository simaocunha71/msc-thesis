  var consonant_pattern = /[^aeiou]/g;
  var vowel_pattern = /[aeiou]/g;

  var consonants = word.match(consonant_pattern);
  var vowels = word.match(vowel_pattern);

  var i = 0;
  var j = 0;

  while (i < consonants.length && j < vowels.length) {
    if (consonants[i] == vowels[j]) {
      return vowels[j];
    }

    if (consonants[i] < vowels[j]) {
      j++;
    } else {
      i++;
    }
  }

  return '';
}



