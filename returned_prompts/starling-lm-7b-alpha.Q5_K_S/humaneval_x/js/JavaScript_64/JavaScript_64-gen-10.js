  const vowels = ["a", "e", "i", "o", "u"];
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i].toLowerCase())) {
      count += 1;
    }
  }

  return count;
}



