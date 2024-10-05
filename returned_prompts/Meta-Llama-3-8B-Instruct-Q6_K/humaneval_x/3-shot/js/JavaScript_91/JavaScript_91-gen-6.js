  let boredCount = 0;
  let currentSentence = "";

  for (const c of S) {
    if (c == '.' || c == '?' || c == '!') {
      if (currentSentence.startsWith("I")) {
        boredCount++;
      }
      currentSentence = "";
    } else {
      currentSentence += c;
    }
  }

  if (currentSentence.startsWith("I")) {
    boredCount++;
  }

  return boredCount;
} 