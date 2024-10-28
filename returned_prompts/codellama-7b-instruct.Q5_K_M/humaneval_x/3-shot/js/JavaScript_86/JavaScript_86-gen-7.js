  var words = s.split(' ');
  var result = '';
  for (var word of words) {
    var word_array = word.split('');
    word_array.sort();
    result += word_array.join('');
    result += ' ';
  }
  result = result.trim();
  return result;
}



