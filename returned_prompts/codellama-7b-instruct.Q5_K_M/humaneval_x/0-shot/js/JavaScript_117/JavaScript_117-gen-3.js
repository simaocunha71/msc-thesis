/*
  const selectWords = (s, n) => {
    if (s.length === 0) {
      return [];
    }
    const words = s.split(' ');
    const consonantWords = words.filter((word) => {
      const vowels = ['a', 'e', 'i', 'o', 'u', 'y'];
      const consonants = word.split('').filter((char) => {
        return !vowels.includes(char);
      });
      return consonants.length === n;
    });
    return consonantWords;
  };
  */
