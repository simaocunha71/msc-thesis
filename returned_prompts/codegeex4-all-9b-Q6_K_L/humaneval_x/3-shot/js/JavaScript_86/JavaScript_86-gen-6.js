  let words = s.split(' ');
  return words.map(w => w.split('').sort().join('')).join(' ');
}