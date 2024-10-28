  const vowels = "aeiou";
  const upper = s.toUpperCase();
  let count = 0;
  for (const c of upper) {
    if (vowels.includes(c)) {
      count += 1;
    }
  }
  if (s.length > 0 && s[s.length - 1].toLowerCase() == "y") {
    count += 1;
  }
  return count;
}