const encode = (message) => {
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  const vowelMap = {
    a: 'e',
    e: 'i',
    i: 'o',
    o: 'u',
    u: 'a'
  };
  const letterMap = {
    A: 'a',
    E: 'e',
    I: 'i',
    O: 'o',
    U: 'u'
  };
  const vowelRegex = new RegExp(vowels.join('|'), 'g');
  const letterRegex = new RegExp(Object.keys(letterMap).join('|'), 'g');
  const swappedVowelRegex = new RegExp(Object.values(vowelMap).join('|'), 'g');
  const swappedLetterRegex = new RegExp(Object.keys(letterMap).join('|'), 'g');

  let encoded = message.toLowerCase();
  encoded = encoded.replace(vowelRegex, (match) => vowelMap[match]);
  encoded = encoded.replace(letterRegex, (match) => letterMap[match]);
  encoded = encoded.replace(swappedVowelRegex, (match) => vowels[vowels.indexOf(match) - 2]);
  encoded = encoded.replace(swappedLetterRegex, (match) => Object.keys(letterMap)[Object.values(letterMap).indexOf(match)]);
  return encoded;
};

module.exports = encode;
