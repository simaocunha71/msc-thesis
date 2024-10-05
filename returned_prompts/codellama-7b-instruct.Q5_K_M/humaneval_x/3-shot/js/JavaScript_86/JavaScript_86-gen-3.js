  var words = s.split(' ');
  var result = '';

  for (var i = 0; i < words.length; i++) {
    var word = words[i];
    var chars = word.split('');
    chars.sort((a, b) => {
      return a.charCodeAt(0) - b.charCodeAt(0);
    });
    var new_word = chars.join('');
    result += new_word + ' ';
  }
  return result.trim();
}



