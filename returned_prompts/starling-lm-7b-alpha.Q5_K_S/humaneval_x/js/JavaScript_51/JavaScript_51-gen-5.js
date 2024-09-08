  const vowels = "aeiouAEIOU"
  return text.split('').filter(c => !vowels.includes(c)).join('');
}



