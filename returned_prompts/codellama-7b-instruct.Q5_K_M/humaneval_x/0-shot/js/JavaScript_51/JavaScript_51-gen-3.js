const removeVowels = (text) => {
  const vowels = 'aeiou';
  const result = text.split('').filter(char => !vowels.includes(char)).join('');
  return result;
}
