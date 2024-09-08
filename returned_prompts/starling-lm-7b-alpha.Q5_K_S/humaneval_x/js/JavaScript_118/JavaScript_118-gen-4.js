  const vowels = 'aeiouAEIOU';
  const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';

  let last_consonant = -1;
  let current_vowel = '';

  for (const c of word) {
    if (consonants.includes(c)) {
      if (current_vowel != '') {
        if (last_consonant > 0 && last_consonant < current_vowel) {
          return current_vowel;
        }
      }
      last_consonant = c;
      current_vowel = '';
    } else if (vowels.includes(c)) {
      current_vowel = c;
    }
  }

  return current_vowel;
}



