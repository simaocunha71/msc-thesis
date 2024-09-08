  const vowels = 'aeiouAEIOU';
  let result = '';

  for (const c of text) {
    if (vowels.indexOf(c) == -1) {
      result += c;
    }
  }

  return result;
}



