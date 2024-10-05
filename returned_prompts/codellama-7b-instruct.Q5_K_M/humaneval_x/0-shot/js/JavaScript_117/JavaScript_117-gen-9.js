const selectWords = (s, n) => {
  const words = [];
  const consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'];
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  const isConsonant = c => consonants.includes(c);
  const isVowel = c => vowels.includes(c);
  const getConsonants = word => word.split('').filter(isConsonant).length;

  const findWords = word => {
    if (getConsonants(word) === n) words.push(word);
    if (words.length === n) return;
    if (word.length === 0) return;
    findWords(word.slice(1));
  };

  s.split(' ').forEach(findWords);
  return words;
};
