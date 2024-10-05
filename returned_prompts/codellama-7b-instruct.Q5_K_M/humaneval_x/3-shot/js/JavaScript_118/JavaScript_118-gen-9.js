  var vowels = ['a', 'e', 'i', 'o', 'u'];
  var consonants = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'];
  var closest_vowel = '';
  var closest_distance = Infinity;

  for (var i = word.length - 1; i >= 0; i--) {
    if (vowels.includes(word[i])) {
      var vowel_distance = Infinity;
      for (var j = i - 1; j >= 0; j--) {
        if (consonants.includes(word[j])) {
          vowel_distance = i - j;
          break;
        }
      }

      for (var j = i + 1; j < word.length; j++) {
        if (consonants.includes(word[j])) {
          var distance = j - i - 1;
          if (distance < vowel_distance) {
            vowel_distance = distance;
          }
        }
      }

      if (vowel_distance < closest_distance) {
        closest_distance = vowel_distance;
        closest_vowel = word[i];
      }
    }
  }

  return closest_vowel;
}



