  let words = s.split(" ");
  let result = [];
  for (let word of words) {
    let consonants = 0;
    for (let char of word) {
      if (char == " " || char == "'" || char == "," || char == "." || char == "!" || char == "?") {
        continue;
      } else if (!isVowel(char)) {
        consonants += 1;
      }
      if (consonants == n) {
        result.push(word);
        break;
      }
    }
  }
  return result;
}

function isVowel(char) {
  return char == "a" || char == "e" || char == "i" || char == "o" || char == "u" || char == "A" || char == "E" || char == "I" || char == "O" || char == "U";
}



