  let words = s.split(' ');
  let result = [];

  for (const word of words) {
    let sorted = word.split('').sort().join('');
    result.push(sorted);
  }

  return result.join(' ');
}


