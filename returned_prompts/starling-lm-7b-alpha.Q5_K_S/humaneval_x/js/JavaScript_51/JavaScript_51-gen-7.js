  const vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  for (let i = 0; i < text.length; i++) {
    if (!vowels.includes(text[i])) {
      result += text[i];
    }
  }
  return result;
}



