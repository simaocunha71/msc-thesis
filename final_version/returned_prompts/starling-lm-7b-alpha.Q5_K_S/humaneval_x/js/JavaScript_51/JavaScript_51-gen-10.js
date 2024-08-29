  const vowels = "aeiouAEIOU"
  let result = "";

  for (const c of text) {
    if (!vowels.includes(c)) {
      result += c;
    }
  }

  return result;
}



