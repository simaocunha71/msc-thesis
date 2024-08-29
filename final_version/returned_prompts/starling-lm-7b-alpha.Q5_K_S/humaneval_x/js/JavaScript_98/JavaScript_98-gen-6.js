  const uppercaseVowels = "ABCDE";
  let count = 0;
  for (let i = 0; i < s.length; i += 2) {
    if (uppercaseVowels.includes(s[i])) {
      count += 1;
    }
  }
  return count;
}



