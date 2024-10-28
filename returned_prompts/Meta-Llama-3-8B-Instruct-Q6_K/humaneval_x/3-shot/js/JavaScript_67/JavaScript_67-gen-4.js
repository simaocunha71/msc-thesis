  let words = s.split(" ");
  let appleCount = 0;
  let orangeCount = 0;
  for (let i = 0; i < words.length; i++) {
    if (words[i].includes("apples")) {
      appleCount = parseInt(words[i].replace("apples", "").trim());
    }
    if (words[i].includes("oranges")) {
      orangeCount = parseInt(words[i].replace("oranges", "").trim());
    }
  }
  return n - appleCount - orangeCount;
}
