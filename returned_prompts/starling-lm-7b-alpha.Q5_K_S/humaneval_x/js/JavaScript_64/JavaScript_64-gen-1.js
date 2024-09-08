  const vowels = ["a", "e", "i", "o", "u", "y"];
  let count = 0;
  for (const c of s) {
    if (vowels.includes(c)) {
      count += 1;
    }
  }

  return count;
}



