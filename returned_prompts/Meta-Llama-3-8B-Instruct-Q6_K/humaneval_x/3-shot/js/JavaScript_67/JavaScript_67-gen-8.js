  let words = s.split(' ');
  let apples = parseInt(words.filter(word => word.includes('apples')).map(word => word.replace('apples', '')).join(''));
  let oranges = parseInt(words.filter(word => word.includes('oranges')).map(word => word.replace('oranges', '')).join(''));
  return n - apples - oranges;
}