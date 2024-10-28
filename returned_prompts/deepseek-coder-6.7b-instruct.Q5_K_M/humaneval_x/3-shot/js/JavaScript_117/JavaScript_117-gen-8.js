  const vowels = 'aeiouAEIOU';
  return s.split(' ').filter(word => {
    let count = 0;
    for (let letter of word) {
      if (!vowels.includes(letter) && !(letter == ' ')) {
        count++;
      }
    }
    return count == n;
  });
}



