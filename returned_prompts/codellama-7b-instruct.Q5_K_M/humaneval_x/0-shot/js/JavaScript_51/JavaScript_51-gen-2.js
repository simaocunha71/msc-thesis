const removeVowels = (text) => {
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  return text.replace(new RegExp(`[${vowels.join('')}]`, 'g'), '');
}
