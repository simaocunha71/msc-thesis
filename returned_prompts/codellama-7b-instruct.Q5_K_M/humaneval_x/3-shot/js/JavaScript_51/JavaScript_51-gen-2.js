  const vowels = 'aeiouAEIOU';
  const result = [];

  for (const c of text) {
    if (!vowels.includes(c)) {
      result.push(c);
    }
  }

  return result.join('');
}



