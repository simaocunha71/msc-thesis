  const vowels = "aeiouAEIOU";

  var result = "";
  for (const c of text) {
    if (!vowels.includes(c)) {
      result += c;
    }
  }

  return result;
}



