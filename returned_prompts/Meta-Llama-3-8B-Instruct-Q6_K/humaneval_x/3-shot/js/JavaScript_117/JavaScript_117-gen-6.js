  var result = [];
  var current_word = '';

  for (const c of s) {
    if (c.match(/[a-zA-Z]/)) {
      current_word += c;
    } else if (current_word.length > 0) {
      var consonants = current_word.replace(/[aeiouAEIOU]/g, '');
      if (consonants.length === n) {
        result.push(current_word);
      }
      current_word = '';
    }
  }

  return result;
} 