  const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';
  const vowels = 'aeiouAEIOU';

  const count = (word) => {
    let count = 0;
    for (let i = 0; i < word.length; i++) {
      if (consonants.includes(word[i]) && !vowels.includes(word[i])) {
        count++;
      }
    }
    return count;
  };

  const words = s.split(' ');
  const result = [];

  for (const word of words) {
    if (count(word) === n) {
      result.push(word);
    }
  }

  return result;
};



