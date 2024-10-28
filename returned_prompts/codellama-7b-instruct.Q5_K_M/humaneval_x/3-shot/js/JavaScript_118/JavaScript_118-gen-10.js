  var closestVowel = "";
  var lastChar = "";
  var lastVowel = "";
  var lastConsonant = "";
  var lastConsonantIndex = 0;

  for (var i = word.length - 1; i >= 0; i--) {
    var c = word.charAt(i);

    if (c === "a" || c === "e" || c === "i" || c === "o" || c === "u") {
      lastVowel = c;
      if (lastConsonant !== "") {
        return lastVowel;
      }
    } else if (c === "b" || c === "c" || c === "d" || c === "f" || c === "g" || c === "h" || c === "j" || c === "k" || c === "l" || c === "m" || c === "n" || c === "p" || c === "q" || c === "r" || c === "s" || c === "t" || c === "v" || c === "w" || c === "x" || c === "y" || c === "z") {
      lastConsonant = c;
      lastConsonantIndex = i;
    }
  }

  return lastVowel;
}



