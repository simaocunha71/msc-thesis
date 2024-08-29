  let result = 0;
  let currentSentence = "";
  for (const s of S.split(" ")) {
    if (s == "I") {
      result += 1;
    }
    currentSentence += s + " ";
    if (currentSentence.endsWith(".")) {
      currentSentence = "";
    } else if (currentSentence.endsWith("?")) {
      currentSentence = "";
    } else if (currentSentence.endsWith("!")) {
      currentSentence = "";
    }
  }
  return result;
}



