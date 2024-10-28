  var vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  var result = [];

  for (const c of text) {
    if (!vowels.includes(c)) {
      result.push(c);
    }
  }

  return result.join('');
}