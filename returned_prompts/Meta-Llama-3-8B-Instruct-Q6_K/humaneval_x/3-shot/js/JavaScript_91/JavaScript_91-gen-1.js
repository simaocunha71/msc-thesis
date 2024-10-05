  let boredomCount = 0;
  let sentences = S.split(/[.!?]/);
  for (let i = 0; i < sentences.length; i++) {
    if (sentences[i].trim().toLowerCase().startsWith("i")) {
      boredomCount++;
    }
  }
  return boredomCount;
}