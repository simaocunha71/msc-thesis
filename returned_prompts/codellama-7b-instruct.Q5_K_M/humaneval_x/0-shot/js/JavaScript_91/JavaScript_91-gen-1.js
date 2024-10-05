
const isBored = (S) => {
  let count = 0;
  let sentences = S.split(".") || S.split("?") || S.split("!");
  sentences.forEach(function(sentence) {
    if (sentence.startsWith("I")) {
      count++;
    }
  });
  return count;
}

