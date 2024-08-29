  const vowels = 'aeiouy';
  return s.toLowerCase().match(new RegExp(`[${vowels}]`, 'g'))
    ? s.toLowerCase().match(new RegExp(`[${vowels}]`, 'g')).length
    : 0;
}



