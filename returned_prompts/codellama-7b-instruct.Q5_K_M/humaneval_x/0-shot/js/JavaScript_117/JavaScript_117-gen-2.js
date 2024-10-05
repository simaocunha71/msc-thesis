/*
  const selectWords = (s, n) => {
    const words = s.split(' ');
    let consonants = 0;
    let word = '';
    let result = [];
    for (let i = 0; i < words.length; i++) {
      consonants = 0;
      word = words[i].split('');
      for (let j = 0; j < word.length; j++) {
        if (word[j] !== 'a' && word[j] !== 'e' && word[j] !== 'i' && word[j] !== 'o' && word[j] !== 'u') {
          consonants++;
        }
      }
      if (consonants === n) {
        result.push(words[i]);
      }
    }
    return result;
  };
  */

B:
/*
  const selectWords = (s, n) => {
    const words = s.split(' ');
    const result = [];
    for (const word of words) {
      if (getConsonantsCount(word) === n) {
        result.push(word);
      }
    }
    return result;
  };

  const getConsonantsCount = (word) => {
    const vowels = 'aeiou';
    let count = 0;
    for (const letter of word) {
      if (vowels.indexOf(letter) === -1) {
        count++;
      }
    }
    return count;
  };
  */

C:
/*
  const selectWords = (s, n) => {
    const words = s.split(' ');
    return words.filter(word => getConsonantsCount(word) === n);
  };

  const getConsonantsCount = (word) => {
    const vowels = 'aeiou';
    let count = 0;
    for (const letter of word) {
      if (vowels.indexOf(letter) === -1) {
        count++;
      }
    }
    return count;
  };
  */

