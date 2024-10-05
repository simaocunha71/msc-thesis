  const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
  const words = s.split(' ');
  const result = words.filter(word =>
    word.length - word.replace(/[aeiou]/ig, '').length === n
  );
  return result;
}