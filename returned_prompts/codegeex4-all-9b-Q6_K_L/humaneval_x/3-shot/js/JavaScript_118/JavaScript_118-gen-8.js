  var vowels = "aeiouAEIOU";
  var closestVowel = "";

  for (let i = word.length - 1; i >= 0; i--) {
    if (vowels.includes(word[i])) {
      closestVowel = word[i];
    } else if (closestVowel !== "") {
      return closestVowel;
    }
  }

  return closestVowel;
}

