  const vowels = ["a", "e", "i", "o", "u"];
  let count = 0;
  for (const c of s) {
    if (vowels.includes(c)) {
      count += 1;
    }
  }

  if (s.endsWith("y")) {
    count += 1;
  }

  return count;
}



