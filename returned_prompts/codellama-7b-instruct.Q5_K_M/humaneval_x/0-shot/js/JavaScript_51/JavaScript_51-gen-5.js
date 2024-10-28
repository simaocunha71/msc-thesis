const removeVowels = text => text
  .replace(/[aeiou]/gi, '')
  .replace(/[aeiou]/gi, '');

B:
const removeVowels = text => {
  let vowels = 'aeiou';
  for (let i = 0; i < vowels.length; i++) {
    text = text.replace(vowels[i], '');
  }
  return text;
};

C:
const removeVowels = text => text.replace(/[aeiou]/gi, '');

D:
const removeVowels = text => text.replace(/[aAeEiIoOuU]/gi, '');

E:
const removeVowels = text => text.replace(/[aeiouAEIOU]/gi, '');
