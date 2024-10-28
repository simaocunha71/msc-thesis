  const vowels = ['A', 'E', 'I', 'O', 'U']
  let count = 0

  for(let i = 0; i < s.length; i += 2) {
    if(vowels.indexOf(s[i].toUpperCase()) > -1) {
      count += 1
    }
  }

  return count
}
